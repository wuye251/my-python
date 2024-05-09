
# def sum_numbers(nums):  # normal function
#     return sum(nums)    # a sad function abusing the built-in sum function :<

# def higher_order_function(f, lst):  # function as a parameter
#     summation = f(lst)
#     return summation
# result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
# print(result)       # 15

# '''This decorator function is a higher order function
# that takes a function as a parameter'''
# # 这是一个装饰器
# def uppercase_decorator(function):
#     print('Inside the decorator function')
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper

# # upppercase_decorator装饰器应用到greeting上，他比greeting更先执行
# @uppercase_decorator
# def greeting():
#     return 'Welcome to Python'
# print(greeting())   # WELCOME TO PYTHON

ls = [1,2,3,4,5]
# map() 函数是一个内置函数，它接受一个函数和可迭代对象作为参数。
mp = map(lambda x: x**2,ls)
print(list(mp))  # [1, 4, 9, 16, 25]

mp2 = filter(lambda x: x%2 == 0,ls)
print(list(mp2))  # [2, 4]