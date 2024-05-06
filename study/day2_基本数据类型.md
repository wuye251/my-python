## 关键词
|      |      |      |      |
| ---- | ---- | ---- | ---- |
|False |class |from  |or    |
|None  |continue|global|pass|
|True  | def    |if     |<font color=red>raise</font>|
|and    |del    |import |return |
|as     |elif   |in     |try    |
|assert |else   |is     |while  |
|<font color=red>async</font>|except|<font color=red>lambda</font>|with|
|<font color=red>await</font>|<font color=red>finally</font>|<font color=red>nonlocal<font>|<font color=red>yield</font>|
|break  |for    |not    |
### raise
raise用作抛出异常。通过`raise`抛出异常后，程序会停止执行，并在引发异常的位置向上层调用栈中查找能够处理该异常的`try/except`块，如果找到则执行该块中的异常处理代码，否则程序将中断并显示异常信息。
总之，raise 关键字是 Python 中一种用于引发异常的方法，可以用于抛出内置异常或自定义异常，帮助我们在代码中处理错误和异常情况。
```python
class MyError(Exception):
    def __init__(self, message):
        self.message = message
        
x = "hello"
if not type(x) is int:
    raise MyError("x必须是整数类型")
```
### yield
一个带有 yield 的函数就是一个 generator，它和普通函数不同，生成一个 generator 看起来像函数调用，但不会执行任何函数代码，直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行。虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield 返回当前的迭代值。

yield 的好处是显而易见的，把一个函数改写为一个 generator 就获得了迭代能力，比起用类的实例保存状态来计算下一个 next() 的值，不仅代码简洁，而且执行流程异常清晰。
```python
def fab(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b      # 使用 yield
        # print b 
        a, b = b, a + b 
        n = n + 1
 
for n in fab(5): 
    print n
```
结果：
```python
>>>f = fab(5) 
>>> f.next() 
1 
>>> f.next() 
1 
>>> f.next() 
2 
>>> f.next() 
3 
>>> f.next() 
5 
>>> f.next() 
Traceback (most recent call last): 
 File "<stdin>", line 1, in <module> 
StopIteration
```
### async && await
[code](./src/async.py)

### lambda
使用 lambda 来创建匿名函数
`lambda arguments: expression`
- lambda是 Python 的关键字，用于定义 lambda 函数。
- arguments 是参数列表，可以包含零个或多个参数，但必须在冒号(:)前指定。
- expression 是一个表达式，用于计算并返回函数的结果。
```python
x = lambda x,y,z: x+y+z
print(x(1,2,3))
```
结果: 6

### finally
和try/except搭配使用。无论except是否被执行，都会执行finally(和go的defer有点类似)
```python
def func1():
   try:
       return 1
   finally:
       return 2
 
def func2():
   try:
       raise ValueError()
   except:
       return 1
   finally:
       return 3
 
print(func1())
print(func2()) # 注意这里 首先except返回了1  但最后会执行finally 导致最终返回3
```

# 类型
- str
- int
- float
- bool  `True/False`
- complex `1+2j`
- list `[1,2,3]`
- tuple `(1,2,3)`
- dict `{'name':'tom','age':18}`
- set `{1,2,3}`

### list&tuple&set&dict
list:[] tuple:() set:{} dict:{'key':val} set:{}
- 追加
    - list: `lst.append(val)`
    - tuple: `tup = tup + (val,)` (元组内容不可修改 所以只能用+赋值)
    - set: `s.add(val)`
    - dict: `d[key] = val`
- 删除
    - list: `lst.pop(index)`
    - tuple: `tup = tup[:index] + tup[index+1:]`
    - set: `s.remove(val)`
    - dict: `del d[key]`
- 遍历
    - list: `for i in lst:`
    - tuple: `for i in tup:`
    - set: `for i in s:`
    - dict: `for key,val in d.items():`
- 切片
    - list: `lst[start:end:step]`
    - tuple: `tup[start:end:step]`
    - set: `s[start:end:step]`
    - dict: `d[key]`
- 排序
    - list: `lst.sort()`
    - tuple: `tup = sorted(tup)`
    - set: `s = sorted(s)`
    - dict: `d = sorted(d.items())`