from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLiteデータベースの作成
DATABASE_URL = "sqlite:///discordbot/data.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

# ユーザーポイント管理用のテーブル
class UserBalance(Base):
    __tablename__ = "user_balances"

    user_id = Column(String, primary_key=True, index=True)
    balance = Column(Integer, default=1000)  # 初期ポイント1000

# テーブル作成
def init_db():
    Base.metadata.create_all(bind=engine)

# ユーザーのポイントを取得
def get_balance(user_id: str):
    session = SessionLocal()
    user = session.query(UserBalance).filter(UserBalance.user_id == user_id).first()
    if not user:
        user = UserBalance(user_id=user_id)
        session.add(user)
        session.commit()
    session.close()
    return user.balance

# ポイントを増減
def update_balance(user_id: str, amount: int):
    session = SessionLocal()
    user = session.query(UserBalance).filter(UserBalance.user_id == user_id).first()
    if not user:
        user = UserBalance(user_id=user_id, balance=1000)
        session.add(user)

    user.balance += amount
    if user.balance < 0:
        user.balance = 0  # マイナスにはならないようにする

    session.commit()
    session.close()
