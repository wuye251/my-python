## 引入
```python
import re
```

## method
- re.match(substring, string, flags=0): 匹配字符串开头
> - substring: 正则表达式
> - string: 要匹配的字符串
> - flags: 匹配模式，如 re.IGNORECASE 忽略大小写
- re.search(substring, string, flags=0): 匹配字符串任意位置(__匹配全字符串，返回第一个匹配结果__)
- `re.findall`(substring, string, flags=0): 匹配所有符合正则表达式的字符串(__匹配全字符串，以列表形式返回所有匹配结果__)
- re.sub(substring, repl, string, count=0, flags=0): 替换字符串
> - substring: 正则表达式
> - repl: 替换字符串
> - string: 要替换的字符串
> - count: 最大替换次数
> - flags: 匹配模式，如 re.IGNORECASE 忽略大小写
- re.split(substring, string, maxsplit=0, flags=0): 按照正则表达式分割字符串
> - substring: 正则表达式
> - string: 要分割的字符串
> - maxsplit: 最大分割次数
> - flags: 匹配模式，如 re.IGNORECASE 忽略大小写

```python
import re

txt = 'I love to teach python and javaScript'
# It returns an object with span, and match
match = re.match('I love to teach', txt, re.I)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (0, 15)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 0, 15
substring = txt[start:end]
print(substring)       # I love to teach
```

## define pattern
> 定义正则表达式规则时,需要带前缀"r"
```python
import re

pattern = r'\d{3}-\d{3,8}'
string = 'My phone number is 138-12345678'
match = re.search(pattern, string)
```