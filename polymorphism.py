# polymorphism
# types:-
#1. Duck Typing
#2. Operator Overloading
#3. Method Overloading
#4. Method Overriding

# Duck Typing
# class Duck:
#     def walk(self):
#         print("thapak thapak thapak thapak")
# class Horse:
#     def walk(self):
#         print("tabdak tabdak tabdak tabdak")
# class cat:
#     def talk(selt):
#         print("Meow Meow")
# def myfunction(obj):
#     obj.walk()
# d = Duck()
# myfunction(d)
# d = Horse()
# myfunction(d)
# --or
# d = cat()
# myfunction(d)
# ----------------------Strong Typing
class Duck:
    def walk(self):
        print("thapak thapak thapak thapak")
class Horse:
    def walk(self):
        print("tabdak tabdak tabdak tabdak")
class Cat:
    def talk(selt):
        print("Meow Meow")
def myfunction(obj):
    # hasattr(obj, "walk") "True or False" checking walk method is available or not.
    if hasattr(obj, "walk"):
        obj.walk()
    if hasattr(obj, "talk"):
        obj.talk()
d = Duck()
myfunction(d)
d = Horse()
myfunction(d)
d = Cat()
myfunction(d)
#------------------ method overloading
# class Myclass:
#     def sum(self, a=None,b=None,c=None):
#         if a!=None and b!=None and c!=None:
#             s=a+b+c
#         elif a!=None and b!=None:
#             s=a+b
#         else:
#             s = "provide at least two values"
#         return s
# obj = Myclass()
# # print(obj.sum(5,5,5))
# # print(obj.sum(5,5))
# print(obj.sum(5))
#--------------------- method overriding
# class Add:
#     def result(self, x, y):
#         print("addition:", x+y)
# class Multi(Add):
#     def result(self, x, y):
#         # super().result(x, y)
#         print("Multiplication:", x*y)
# m = Multi()
# m.result(10, 20)
#--------------------- constructor overriding
# class Father:
#     def __init__(seft):
#         money = 2000
#         print("Father class Constructor")
#     def show(self):
#         print("Father class Instance Method")
# class Son(Father):
#     def disp(self):
#         print("son class Instance Method")
# s = Son()
# ---------or-----
# class Father:
#     def __init__(seft):
#         money = 2000
#         print("Father class Constructor")
#     def show(self):
#         print("Father class Instance Method")
# class Son(Father):
#     def __init__(self):
#         print("Child class constructor")
#     def disp(self):
#         print("son class Instance Method")
# s = Son()
