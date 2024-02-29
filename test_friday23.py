def student(name,age,school,form):
    print(name)
    print(age)
    print(school)
    print(form)
    print("Hello there reader, my name is " + name + " and I am " + str(age) + " years old. I school at " + school + " and i am in form " +str(form))
student("John",17,"Moringa","3")


class Student:
    def __init__(self,student_name,marks):
        self.student_name = student_name
        self.marks = marks
stud1 = Student("John",567)
stud2 = Student("Ann",897)
print(f"My name is {stud1.student_name} and I scored {stud1.marks} out of 1100")
print(f"My name is {stud2.student_name} and I score {stud2.marks} out of 1100")

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        area = self.length * self.width
        print(f"Rectangle: my area is {area}")

    def perimeter(self):
        perimeter = (self.length + self.width)* 2
        print(f"Rectangle: my perimeter is {perimeter}")

rect1 = Rectangle(11,12)
rect2 = Rectangle(10,10)
rect1.area()
rect2.perimeter()


import math
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        area = math.pi * self.radius**2
        print(f"Circle: Hello there my area is {area}")
    def circumference(self):
        circumference = math.pi * 2*self.radius
        print(f"Circle: Hello, my circumference is {circumference}")
Circle1 = Circle(7)
Circle2 = Circle(14)
Circle1.area()
Circle2.circumference()


class BankAccount:
    def __init__(self,account_number,balance,date_of_opening,customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
    def deposit(self):
        deposit = int(input("Enter your deposit: "))
        balance = self.balance + deposit
        print(f"Hello {self.customer_name}, your new balance is {balance}")

    def withdraw(self):
        withdraw = int(input("Enter your withdrawal amount: "))
        balance = self.balance - withdraw
        print(f"Hello {self.customer_name}, your new balance is {balance}")
mybanc = BankAccount(247247,17000,"4/4/2004","William")
mybanc2 = BankAccount(247247,100000,"18/12/2005","Yvonne")
mybanc2.withdraw()
# mybanc.deposit()

