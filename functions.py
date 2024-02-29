# def my_function():
#     print('This is my first function')
#     print('This is my first function')
#     print('This is my first function')
# my_function()
# my_function()
# def karibu(Name):
#     print(Name)
#     print(Name)
#     print(Name)
# karibu('William')
# # karibu('John')
# # karibu('Vernon')
#
# def num(nambari):
#     print(nambari)
# num(2)
#
#
# def salutation(first_name):
#     print("Good morning " + first_name + ". How are you doing today?")
# salutation("Esther")
# def profile(name,age,location):
#     print("Hello " + name + " you are " + str(age) + " years old from " + location)
# profile('William',18,'Nairobi')
# #
# def details(name):
#     math = int(input("Enter your math mark: "))
#     eng = int(input("Enter your English mark: "))
#     Computer = int(input("Enter your Computer Studies mark: "))
#     if math>=75:
#         add = (math+eng+Computer)
#         average = add/3
#         if average>=78:
#             print("Hello " + name + " you're average is " + str(average)  +", you have passed the test!")
#         #    Scholarhip
#
#             email = str(input("Enter your email address: "))
#             last_name = str(input("Enter your last name: "))
#             Guardian_name = str(input("Enter your Guardian's name: "))
#             Guardian_email = str(input("Enter your Guardian's email address: "))
#             print("Confirm you're scholarship by clicking the button")
#             print("Congratulations " + name + ". You re one of the few who have been awarded  a scholarship.We sent you an email.")
#         else:
#             print("Hello " + name + " you're average is " + str(average)  +", you have failed the test!")
#     else:
#         print("Your math is too low " + name + ". Work on it")
# details('William')

#
# def employees(name,age):
#     if age >= 20:
#         print(name + " you are " + str(age) + " years old.Viable")
#     elif age < 20 and age >=15:
#         print(name + " you are " + str(age) + " years old.Senior minor")
#     elif age <15 and age>10:
#         print(name + " you are " + str(age) + " years old.Teen")
#     else:
#         print(name + " you are " + str(age) + " years old.Too young")
# employees('John',32)
# employees('Zawadi',18)
# employees('Neema',6)
#
#
# def age_calculator(age):
#     new_age = age + 10
#     return new_age
# print(age_calculator(46))

#
# def marks(*subjects):
#     total = sum(subjects)
#     return total
# print(marks(23,45,67,78))
# print(marks(78,89,90))


# def calc(name, profit1, profit2):
#     totals = float(profit1) + float(profit2)
#     print("Hello " + name + "your total profit is: " + str(totals))
#     return totals
#
# calc("John",157.9,167.332)



# def locage(age):
#     if age>=60:
#         print("You are " + str(age) + " years old. You have been posted to Kisumu")
#     elif age>=50 and age<60:
#         print("You are " + str(age) + " years old. You have been posted to  Nakuru")
#     elif age>=40 and age<50:
#         print("You are " + str(age) + " years old. You have been posted to Mombasa")
#     else:
#         print("You are " + str(age) + " years old. You have been posted to Nairobi")
# locage(24)

def myfunction(food):
    for x in food:
        print(x)
fruits = ["Apples","Bananas","Mangoes"]
myfunction(fruits)
