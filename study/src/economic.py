my_list1 = [1, 2, 3]
my_list2 = ['a', 'b', 'c']
my_list3 = ['x', 'y', 'z']
z = zip(my_list1, my_list2, my_list3)
for i in zip(my_list1, my_list2, my_list3):
    print(i)

my_list = ['apple', 'banana', 'cherry']
for i, v in enumerate(my_list):
    print(i, v)

def my_func(*args):
    for i in args:
        print(i)

my_func(1, 2, 3, 4, 5)
my_func('a', 'b', 'c')


def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
    # Printing dictionary items
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))

