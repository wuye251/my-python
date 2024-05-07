## 定义
```python
empty_dict = {}
empty_dict2 = dict()

dic = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}
```
## len 
print(len(dic))

## 访问
```python
print(dic['name']) # 如果不存在会报错
print(dic.get('age')) # 如果不存在会返回None
print(dic.get('gender', 'unknown')) # 如果不存在会返回默认值
```

## 判断key是否存在
```python
if 'name' in dic:
    print(True) # 存在
else:
    print(False) # 不存在
```

## 判断value是否存在
```python
if 'Beijing' in dic.values():
    print(True) # 存在
else:
    print(False) # 不存在
```

## 删除key
```python
dic.pop('age')
del dic['name']

dic.popitem() # 删除最后一个元素
```
