# def eomji_decorator(func):
#     def wrapper(name):
#         func(name)
#         print('^-^//')
#     return wrapper


# @eomji_decorator
# def ko_hello(name):
#     print(f'안녕하세요, {name}님!')
# @eomji_decorator
# def en_hello(name):
#     print(f'Hello, {name}!')

# # def add_emoji(name, func):
# #     func(name)
# #     print('^-^//')

# ko_hello('tak')
# en_hello('tak')


# (eomji_decorator(ko_hello))('tak')
# new_func=eomji_decorator(ko_hello)
# new_func('tom')

# class Myclass:

#     def method(self):
#         return 'instance method',self

#     @classmethod
#     def classmethod(cls):
#         return 'class method', cls

#     @staticmethod
#     def staticmethod():
#         return 'static method'

# my_class=Myclass()
# print(my_class.method())
# print(my_class.classmethod())
# print(my_class.staticmethod())
# class Person:
#     def __init__(self):
#         self._age=0

        
#     def get_age(self): #getter
#         print('getter 호출 !')
#         return self._age

#     def set_age(self,age): #setter
#         print('setter 호출 !')
#         self._age = age

    # age = property(get_age,set_age)

# p1 = Person()
# p1.age = 25
# print(p1.age)
# p1._age = 25 #이거안됨
# print(p1._age)#이거안됨

# #불편함
# p1.set_age(25)
# print(p1.set_age())
class Person:
    def __init__(self):
        self._age=0

    @property
    def age(self): #getter
        print('getter 호출 !')
        return self._age

    @age.setter
    def age(self,age): #setter
        print('setter 호출 !')
        self._age = age
        
p1 = Person()
p1.age = 25
print(p1.age)