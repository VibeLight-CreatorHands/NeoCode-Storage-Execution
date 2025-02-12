from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///discordbot/data.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

# ユーザーのポイント & 仮想通貨データ
class UserBalance(Base):
    __tablename__ = "user_balances"

    user_id = Column(String, primary_key=True, index=True)
    balance = Column(Integer, default=1000)  # 初期ポイント
    crypto = Column(Float, default=0.0)  # 仮想通貨（YUYUCOINなど）

# 仮想通貨の価格変動データ
class CryptoMarket(Base):
    __tablename__ = "crypto_market"

    id = Column(Integer, primary_key=True)
    rate = Column(Float, default=100.0)  # 初期レート 1YUYUCOIN = 100P

# テーブル作成
def init_db():
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()

    # 初回実行時のみ市場データを作成
    if not session.query(CryptoMarket).first():
        session.add(CryptoMarket(rate=100.0))
        session.commit()

    session.close()

# 現在の仮想通貨レートを取得
def get_crypto_rate():
    session = SessionLocal()
    market = session.query(CryptoMarket).first()
    session.close()
    return market.rate if market else 100.0  # デフォルト100P = 1YUYUCOIN

# 仮想通貨レートを更新（管理者向け）
def update_crypto_rate(new_rate: float):
    session = SessionLocal()
    market = session.query(CryptoMarket).first()
    if market:
        market.rate = new_rate
    else:
        session.add(CryptoMarket(rate=new_rate))
    session.commit()
    session.close()

# ユーザーの現在のポイントを取得する関数
def get_balance(user_id: str):
    session = SessionLocal()
    user = session.query(UserBalance).filter(UserBalance.user_id == user_id).first()
    session.close()
    return user.balance if user else 0  # ユーザーが存在しない場合は0を返す

# ユーザーのポイント残高を更新する関数（追加！）
def update_balance(user_id: str, amount: int):
    session = SessionLocal()
    user = session.query(UserBalance).filter(UserBalance.user_id == user_id).first()
            
    if not user:
        user = UserBalance(user_id=user_id)
        session.add(user)

    user.balance += amount
    session.commit()
    session.close()
    return user.balance  # 更新後の残高を返す

# ユーザーのポイントと仮想通貨を取得
def get_user_data(user_id: str):
    session = SessionLocal()
    user = session.query(UserBalance).filter(UserBalance.user_id == user_id).first()
    if not user:
        user = UserBalance(user_id=user_id)
        session.add(user)
        session.commit()
    session.close()
    return user.balance, user.crypto

# ポイント↔仮想通貨の変換
def convert_currency(user_id: str, amount: float, to_crypto: bool):
    session = SessionLocal()
    user = session.query(UserBalance).filter(UserBalance.user_id == user_id).first()
    if not user:
        user = UserBalance(user_id=user_id)
        session.add(user)

    rate = get_crypto_rate()
    
    if to_crypto:
        # ポイント → 仮想通貨
        if user.balance < amount:
            session.close()
            return False  # 失敗（ポイント不足）
        user.balance -= amount
        user.crypto += amount / rate
    else:
        # 仮想通貨 → ポイント
        if user.crypto < amount:
            session.close()
            return False  # 失敗（仮想通貨不足）
        user.crypto -= amount
        user.balance += int(amount * rate)

    session.commit()
    session.close()
    return True  # 成功