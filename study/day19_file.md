## open: 打开文件
```python
f = open('filename.txt', 'r/a/w/x/t/b')

f = open('filename.txt', 'r') # 等于 f = open('filename.txt')
```

- 'r'：读模式，文件必须存在，否则报错。（默认模式）
- 'a'：追加模式，如果文件不存在，则创建新文件。
- 'w'：写模式，如果文件不存在，则创建新文件，如果文件存在，则覆盖原有内容。
- 'x'：创建模式，如果文件不存在，则创建新文件，如果文件存在，则报错。
- 't'：文本模式，默认模式，以文本方式打开文件。
- 'b'：二进制模式，以二进制方式打开文件。

## read()/read(number)/readline/readlines: 读取文件内容
- read()读取文件所有内容
- read(number) 读取文件指定数量的字符
- readline() 读取文件一行内容
- readlines() 读取文件所有行内容，并返回列表

### read().splitlines(): 读取文件内容 并按行拆分为列表
```python
with open('filename.txt', 'r') as f:
    content = f.read().splitlines()
```

## remove: 删除文件
```python
import os

if os.path.exists('filename.txt'):
    os.remove('filename.txt')
```

## json.loads({json}):json convert to dict
```python
import json
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct)) #dict
print(person_dct)
```
## json.dumps({dict}):dict convert to json
```python
import json
# dictionary
person_dct = {
    "name": "Asabeneh",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# let's change dictionary to JSON
person_json = json.dumps(person_dct)
print(type(person_json)) #str
print(person_json)
```