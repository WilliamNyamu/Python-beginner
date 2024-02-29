# a class is anything with properties
# must start with Upper case
#
# class Person:
#     name = "John"
#     age = 18
#     gender = "Female"
#     Marital_status = "Married"
# print(Person.name)
# print(Person.age)
# print(Person.gender)
# print(Person.Marital_status)
# Person.age =20
# print(Person.age)
#
#
# class Employees:
#     F_name = "John"
#     L_name = "Nduati"
#     age = 19
#     Salary = 10000
#     gender = "Male"
# print(f"{Employees.F_name} {Employees.L_name} your age is {Employees.age} and you earn a salary of {Employees.Salary}.Moreover, you are of {Employees.gender} gender")
# print(f"{Employees.L_name} you are {Person.gender} who earns {Employees.Salary}")
#
# class Parent:
#     firstname = "Esther"
#     lastname = "Kiprop"
# Parent1 = Parent()
# print(Parent1.firstname)
# print(Parent1.lastname)
#
#
# class Parent:
#     def __init__(self,firstname,lastname,age):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
# Parent1 = Parent("John","Nduati",18)
# Parent2 = Parent("Ann","Kenyatta",26)
# Parent3 = Parent("William","Nyamu",26)
# print(f"{Parent1.firstname} your are {Parent1.age} years old")
# print(Parent1.firstname)
# print(Parent2.firstname)
# print(Parent3.firstname)
# print(Parent1.lastname)
# print(Parent2.lastname)
# print(Parent3.lastname)
#
# class Cars:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
# Car1 = Cars("Ford","Range",2023)
# Car2 = Cars("Toyota","Axis",2020)
# Car3 = Cars("Nissan","Sunny",1996)
# print(f"The car model is {Car1.make} {Car1.model} manufactured in the year {Car1.year}")
#
# class Students:
#     def __init__(self,name,form,house):
#         self.name = name
#         self.form = form
#         self.house = house
# Student1 = Students("Ramadhan",4,"Patshaw")
# Student2 = Students("Nicholas",4,"Dulverton")
# Student3 = Students("Abdiwahab",4,"Geturo")
# print(f"{Student2.name} summoned {Student1.name} in the {Student2.house} Wing and asked him to appreciate {Student3.name} form {Student3.form}G and {Student3.house} house for his art in designing the certificates")
#
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def myfunc(self):
#     print("Hello my name is " + self.name)
#
# p1 = Person("John", 36)
# p1.myfunc()
#
# def food(drink):
#     for x in drink:
#         print(x)
# drinks = ["Soda","Pepsi","Energy drinks","Water"]
# food(drinks)

#
# x = lambda a:a+10
# print(x(5))
#
# y =  lambda a,b:a*b
# print(y(5,3))
#
#
# def myfunc(n):
#     return lambda a:a*n
# mydoubler = myfunc(2)
# print(mydoubler(11))
#
#
# cars = ["Toyota","BMW","Volvo"]
# for z in cars:
#     print(z)
# cars.append("Bentley")
# print(cars)
#
class Persons:
    def __init__(msilly,fname,lname):
        msilly.fname = fname
        msilly.lname = lname
    def printname(msilly):
        print(msilly.fname,msilly.lname)
x = Persons("John","Doe")
x.printname()
class Student(Persons):
    pass
y = Student("William","Liam")
y.printname()

class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc(self):
        print(f"Hello my name is {self.name}")
        print("Hello I am " + str(self.age) + " years old")
p1 = People("Brian",16)
p1.myfunc()




class Magari:
    def __init__(self,make,model,price,year):
        self.make = make
        self.model = model
        self.price = price
        self.year = year
    def desribe(self):
        print(f"My favourite car is {self.make} and of model {self.model}. It costs {self.price}")
obj1 = Magari("Ford","Ranger","$2000",2013)
obj2 = Magari("Toyota","Axis","$1400",2010)
obj3 = Magari("Nissan","Sunny","$2500",2019)
obj1.desribe()
obj2.desribe()
obj3.desribe()


class Person:
    def __init__(self,fname,lname,gender,age):
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.age = age
    def myfunc(self):
        print(f"Your username is {self.fname} {self.lname}")
        print(f"Your are a {self.gender} and  {self.age} years old")
    def display_age(self):
        print(self.age)
    def display_gender(self):
        print(self.gender)
    def display_lname(self):
        print(self.lname)
    def increment_age(self):
        self.age += 10
p1 = Person("John","Doe","Male",28)
p2 = Person("Liza","Beryl","Female",45)
p1.myfunc()
p2.display_age()
p1.display_lname()
p2.display_gender()
my_tuple = ("apple","banana","oranges")
for q in my_tuple:
    print(q)

my_iter = iter(my_tuple)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

mystr = "banana"
for letter in mystr:
    print(letter)
myitr = iter(mystr)
print(next(myitr))
print(next(myitr))
print(next(myitr))
print(next(myitr))
print(next(myitr))
print(next(myitr))

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

class Mynum:
    def __iter__(self):
        self.x = 2
        return self
    def __next__(self):
        z = self.x
        z += 2
        return z
m_class = Mynum()
my_ite = iter(m_class)
print(next(my_ite))

def mygreetings:
