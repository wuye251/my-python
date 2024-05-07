> A tuple is a collection of different data types which is ordered and unchangeable (immutable).
> 是一个不同数据类型集合，是有序的且不可变的（不可修改）。

## 定义
```python
# 定义一个空元组
my_tuple = ()
my_tuple = tuple()
```

## len: 获取长度
```python
my_tuple = (1, 2, 3, 4, 5)
print(len(my_tuple))  # 输出5
```

## 截取
```python
my_tuple = (0, 1, 2, 3, 4, 5)
print(my_tuple[1:3])  # 输出(1, 2) 不包含3
```

## 如果要修改则需要改为list后修改
```python
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
my_list[0] = 10
my_tuple = tuple(my_list)
print(my_tuple)  # 输出(10, 2, 3, 4, 5)
```

## +: 合并
```python
my_tuple1 = (1, 2, 3)
my_tuple2 = (4, 5, 6)
my_tuple3 = my_tuple1 + my_tuple2
print(my_tuple3)  # 输出(1, 2, 3, 4, 5, 6)
```
