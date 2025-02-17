# NeoCode-Storage-Execution
Yuyuto.jp server multi-script code storage system and its execution API package.

# 概要
言葉の通り、多くの言語をサポートした自立進化型ストレージ&実行システムです。主にリポ主は自作の大規模サーバーのAPIパッケージやバックエンドとして利用してます。
システムには、ExecutionAPIというAPIがあり、これを使用してオリジナルライブラリやストレージにアクセスしてスクリプト実行したり、コミットしたりできます。
また、このシステムは「自己進化型」なので、AIや鯖主、管理者なんかが別システム上でコミットしています。皆さんがコミットできるのは第三システムのみなのでご注意ください。
# ExecutionAPI RequestBody

ここでは、基本的なCodeStoradge-Executionの使い方について紹介します。
## 第一前提として
### 日本語にはほとんど対応していません。ご了承ください。
このAPIでは以下のプログラム言語をサポートしています。
- Python
- C++
- JavaScript(Node.js)
- TypeScript(Node.ts)
- Go
- Ruby
- Java
- bash
- PHP
- Perl
また、このAPIは以下のソリューションもサポートしています。
- Discord(実装中・ベータ版使用可能)
- Grindgham.com(実装中)
- LINE(実装中)

※ソリューションにおいてはまだ実装中のものもあります。
よくわからんもんがいっぱいあるとは思いますが、使って試してってください。

---
## 一覧

### 1. `keisan.py`  
- 四則演算を行うスクリプトです。
- operation:add(+),subtract(-),multipiv(×),divide(÷)が使えます。
- num1とnum2にそれぞれ数字を代入してください。
リクエストボディ:10+20=xを計算するとき
```json
{
  "input_value": "{\"operation\": \"add\", \"num1\": 10, \"num2\": 20}",
  "language": "python"
}
```

---

### 2. `morse.py`  
- 文章をモールス信号に変換します。
- textに英文を入れてください。
リクエストボディ:
```json
{
  "input_value": "{\"text\": \"Hello World\"}",
  "language": "python"
}
```

---

### 3. `ascii_art_generator.py`  
- ユーザーが入力したテキストをASCIIアート形式で表示します。テキストをアートとして視覚的に表現します。
- textに任意の文字を配置してください。なお、レスポンスとして変化しない場合があります。
リクエストボディ:
```json
{
  "input_value": "{\"text\": \"yuyutos\"}",
  "language": "python"
}
```

---

### 4. `anagram_checker.py`  
- 2つの単語がアナグラムかどうか（文字を並べ替えて同じ単語になるか）を判定します。
- word1に元となる単語を、word2に照合したい単語または文字列を代入してください。
リクエストボディ:
```json
{
  "input_value": "{\"word1\": \"listen\", \"word2\": \"silent\"}",
  "language": "python"
}
```

---

### 5. `caesar_cipher.py` 
- 指定した文字列をシーザー暗号（文字を指定した数だけシフト）で暗号化または復号化します。
- textに元の英単語を代入し、shiftに暗号キーとなる数字を入力してください(1~25)。
- 暗号文をtextに、shiftに26から暗号キーを引いた数字を入力すると復号できます。
リクエストボディ:
```json
{
  "input_value": "{\"text\": \"hello\", \"shift\": 3}",
  "language": "python"
}
```

---

### 6. `word_frequency.py`  
- 入力されたテキスト内の単語の出現回数を解析し、頻度順にリスト表示します。
- textに参照する英文を入力してください。
リクエストボディ:
```json
{
  "input_value": "{\"text\": \"hello world hello again\"}",
  "language": "python"
}
```

---

### 7. `temperature_converter.py`  
- 指定された温度（摂氏または華氏）を他の単位（華氏や摂氏、ケルビン）に変換します。
- temperatureに温度の数字を、unitに変換する単位を入力します。
- 単語には、以下が使えます。:celsius・fahrenheit
- celsiusを指定すると摂氏が、fahrenheitを指定すると華氏に変換されます。
- unitに何も指定しないとケルビンに変換されます。
リクエストボディ:
```json
{
  "input_value": "{\"temperature\": 100, \"unit\": \"Celsius\"}",
  "language": "python"
}
```

---

### 8. `unique_elements.py`  
- リストに含まれる重複を削除し、ユニークな要素のみを抽出して返します。
- elementsにリストを記述してください。記述方法はPythonリスト記述法に準じます。
リクエストボディ:
```json
{
  "input_value": "{\"elements\": [1, 2, 2, 3, 4, 4, 5]}",
  "language": "python"
}
```

---

### 9. `random_password_generator.py`  
- 名前の通り、協力なパスワードを作成します。
- lengthにパスワードの長さを数字で指定してください。
リクエストボディ:
```json
{
  "input_value": "{\"length\": 12}",
  "language": "python"
}
```

---

### 10. `color_converter.py`
- RGBカラーコードを16進数形式（Hex）に変換します。
- r,g,bそれぞれに0~255までの数字を入力してください。  
リクエストボディ:
```json
{
  "input_value": "{\"r\": 255, \"g\": 100, \"b\": 50}",
  "language": "python"
}
```

---

### 11. `quote_of_the_day.py`  
- 世界の名言を返します。
- リクエストボディは必要ありません。以下をコピペしてお願いします。
リクエストボディ:
```json
{
  "input_value": "{}",
  "language": "python"
}
```

---

### 12. `string_processor.py`  
- ユーザーが入力した文字列を逆順にしたり、大文字小文字を変換したりします。
- operationに変換したいモードを指定してください。
- operationには以下が入ります:uppercase,lowercase,reverse
リクエストボディ:
```json
{
  "input_value": "{\"operation\": \"uppercase\", \"text\": \"Hello OpenAI\"}",
  "language": "python"
}
```

---

### 13. `prime_checker.py`  
- 指定された数が素数かどうかを判定します。素数であれば「True」、そうでなければ「False」を返します。
- numberに素数判定したい数を入力します。
リクエストボディ:
```json
{
  "input_value": "{\"number\": 29}",
  "language": "python"
}
```

---

### 14. `factorial.py`  
- 指定された数の階乗を計算します（n! = n * (n-1) * ... * 1）。
- numberに階乗を計算したい数を指定します(最大1500)。
リクエストボディ:
```json
{
  "input_value": "{\"number\": 5}",
  "language": "python"
}
```

---

### 15. `palindrome_checker.py`  
- 入力された文字列が回文かどうか（前から読んでも後ろから読んでも同じか）を判定します。
- textに文章を指定します。日本語に対応しています。
リクエストボディ:
```json
{
  "input_value": "{\"text\": \"radar\"}",
  "language": "python"
}
```

---

### 16. `fibonacci_generator.py`  
- 指定された数だけフィボナッチ数列を生成してリスト形式で返します。
- countに返してほしいフィボナッチ数列の回数を指定します。100までであれば対応しています。
リクエストボディ:
```json
{
  "input_value": "{\"count\": 10}",
  "language": "python"
}
```

---

### 17. `weather_simulator.py`  
- 天気を指定された都市名と単位（摂氏または華氏）で、シンプルな天気予報をシミュレートします。
- cityに有効な都市名を、unitには7番と同じものを指定します。
リクエストボディ:
```json
{
  "input_value": "{\"city\": \"New York\", \"unit\": \"Celsius\"}",
  "language": "python"
}
```

---

### 18. `random_number_generator.py`  
- 指定された範囲のランダムな整数を生成します。範囲内で任意の数を生成します。
- min・maxともに整数を指定します。このスクリプトでは、必ずminよりmaxが小さくなってはいけません。
リクエストボディ:
```json
{
  "input_value": "{\"min\": 1, \"max\": 100}",
  "language": "python"
}
```

---

### 19. `currency_converter.py`  
- 現在の為替レートをもとに、通貨を両替します。
- amountに金額を、from_currencyに両替元の通貨名を
リクエストボディ:
```json
{
  "input_value": "{\"amount\": 100, \"from_currency\": \"USD\", \"to_currency\": \"JPY\"}",
  "language": "python"
}
```

---

### 20. `password_strength_checker.py`  
- ユーザーが入力したパスワードの強度を判定し、強度レベル（弱い、普通、強い）を返します。
- passwordに検証したいパスワードを入力してください。
リクエストボディ:
```json
{
  "input_value": "{\"password\": \"SecureP@ssw0rd\"}",
  "language": "python"
}
```

---

これらは完全に例なので自分の送りたいものに変えてください。
Pythonにおいては、スクリプト上の問題でsys.read()を使っているため、このようなリクエストボディになります。