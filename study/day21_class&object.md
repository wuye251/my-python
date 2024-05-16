## __init__:构造方法
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Alice", 25)
print(p1.name)  # Alice
print(p1.age)  # 25
```

## 对象方法
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, my name is " + self.name)

p1 = Person("Alice", 25)
p1.say_hello()  # Hello, my name is Alice
```

## 继承
```python
class Animal:
    def __init__(self, name):
        self.name = name


    def say_hello(self):
        print("Hello, my name is " + self.name)

# Dog继承了Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

dog = Dog("Rufus", "Labrador")
dog.say_hello()  # Hello, my name is Rufus
```