# age = 17
# if age >= 18:
#     print("You are " + str(age) + " years old.")
#     print("You are  old enough to move out")
#     print("You are old enough to have an ID")
#
#
# elif age>=15:
#     print("You are a senior minor")
# elif age<=10:
#     print("You are " + str(age) + " years old")
#     print("Please get your parents' or guardian's consent")
# else:
#     print("You are " + str(age) + " years old")
#     print("You are underage")
#     print("You are young to move out")

# marks = 42.5
# no = 1
# while no <= 2:
#     no = no + 1
#     name = input("Enter your name: ")
#     form = input("Enter your form: ")
#     mark = int(input("Enter your mark: "))
#     if mark >= 80 and mark <= 100:
#         print(mark)
#         print("Hello " + name + " you have an A. Congratulations!")
#     elif mark >= 70:
#         print(mark)
#         print("Hello " + name + " you have a B. Good work!")
#     elif mark >= 60:
#         print(mark)
#         print("Hello " + name + " you have a C. Average.")
#     elif mark >= 50:
#         print(mark)
#         print("Hello " + name + " you have a D. Work harder!")
#     else:
#         print(mark)
#         print("Hello " + name + " you have an E. PULL UP YOUR SOCKS!")
# print("End of the loop!")


temperature = int(input("Enter your temperature reading: "))

if temperature >= 30:
    print("Please have  vest on. The temp. readings are so high")
elif temperature >= 20:
    print("Please do not wear a sweater ")
else:
    print("Please put on a jacket.")