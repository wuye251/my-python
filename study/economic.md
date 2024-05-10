## Packing List(*args):定义任意参数个数
```python
def my_func(*args):
    for i in args:
        print(i)

my_func(1, 2, 3, 4, 5)
my_func('a', 'b', 'c')
```

## Packing Dict(**kwargs):定义任意关键字参数
```python
def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
    # Printing dictionary items
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))
```

## enumerate():遍历迭代器并返回索引和值
> 一般直接for循环list 只有key 但是没有val  用`for i,v in enumerate(list)` 就可以获得索引和值
```python
my_list = ['apple', 'banana', 'cherry']
for i, v in enumerate(my_list):
    print(i, v)
```

## zip():将多个迭代器打包成一个元组
```python
my_list1 = [1, 2, 3]
my_list2 = ['a', 'b', 'c']
my_list3 = ['x', 'y', 'z']
for i in zip(my_list1, my_list2, my_list3):
    print(i)

'''
out: 
(1, 'a', 'x')
(2, 'b', 'y')
(3, 'c', 'z')
'''
```