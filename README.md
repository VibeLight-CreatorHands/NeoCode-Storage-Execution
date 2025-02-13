# Code-Storage-Execution
Yuyuto.jp server multi-script code storage system and its execution API package

# API RequestBody

---

### 1. `keisan.py`  
リクエストボディ:
```json
{
  "input_value": "{\"operation\": \"add\", \"num1\": 10, \"num2\": 20}"
}
```

---

### 2. `text_to_morse.py`  
リクエストボディ:
```json
{
  "input_value": "{\"text\": \"Hello World\"}"
}
```

---

### 3. `ascii_art_generator.py`  
リクエストボディ:
```json
{
  "input_value": "{\"text\": \"OpenAI\"}"
}
```

---

### 4. `anagram_checker.py`  
リクエストボディ:
```json
{
  "input_value": "{\"word1\": \"listen\", \"word2\": \"silent\"}"
}
```

---

### 5. `caesar_cipher.py`  
リクエストボディ:
```json
{
  "input_value": "{\"text\": \"hello\", \"shift\": 3}"
}
```

---

### 6. `word_frequency.py`  
リクエストボディ:
```json
{
  "input_value": "{\"text\": \"hello world hello again\"}"
}
```

---

### 7. `temperature_converter.py`  
リクエストボディ:
```json
{
  "input_value": "{\"temperature\": 100, \"unit\": \"Celsius\"}"
}
```

---

### 8. `unique_elements.py`  
リクエストボディ:
```json
{
  "input_value": "{\"elements\": [1, 2, 2, 3, 4, 4, 5]}"
}
```

---

### 9. `random_password_generator.py`  
リクエストボディ:
```json
{
  "input_value": "{\"length\": 12}"
}
```

---

### 10. `color_converter.py`  
リクエストボディ:
```json
{
  "input_value": "{\"r\": 255, \"g\": 100, \"b\": 50}"
}
```

---

### 11. `quote_of_the_day.py`  
リクエストボディ（このスクリプトは入力を必要としないので、空のJSONオブジェクトでも動作します）:
```json
{
  "input_value": "{}"
}
```

---

これらのリクエストボディは、すべてJSON文字列として`sys.stdin.read()`に渡されることを想定しています。
また、これらは完全に例なので気を付けてください。
