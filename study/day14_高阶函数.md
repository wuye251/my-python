## 将函数作为参数传递

```python
def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15
```

## 函数作为返回值返回
```python
def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3
```

## 闭包函数
> 在一个函数中嵌套一个方法，嵌套的方法称为闭包函数
```python
def outer_function(x):
    def inner_function(y):
        return x + y

    return inner_function
result = outer_function(3)
print(result(4))       # 7
```

## 装饰器函数
> 装饰器函数是一种高阶函数，它可以用来修改另一个函数的行为，或者添加额外功能。
```python
# 这是一个装饰器
def uppercase_decorator(function):
    print('Inside the decorator function')
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# upppercase_decorator装饰器应用到greeting上，他比greeting更先执行
@uppercase_decorator
#@xxx 也可以应用多个装饰器到一个函数上
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON
```

### 定义带参数的装饰器函数
```python
def decorator_with_parameters(function): # 接受被装饰的print_full_name函数的参数
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3) # 用这个来定义函数参数
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh",'Finland')
```

## 匿名函数
> lambda表达式或匿名函数是一种创建函数的简便方式。
> map() 函数是一个内置函数，它接受一个函数和可迭代对象作为参数。
> filter() 函数也是一个内置函数，它接受一个函数和可迭代对象作为参数。(True/False)
> reduce() 函数也是一个内置函数，它接受一个函数和可迭代对象作为参数。(列表归为一个数)
```python
# 匿名函数
ls = [1,2,3,4,5]
# map() 函数是一个内置函数，它接受一个函数和可迭代对象作为参数。
mp = map(lambda x: x**2,ls)
print(list(mp))  # [1, 4, 9, 16, 25]

mp2 = filter(lambda x: x%2 == 0,ls)
print(list(mp2))  # [2, 4]

mp3 = reduce(lambda x,y: x+y,ls)
print(mp3)  # 15
```

