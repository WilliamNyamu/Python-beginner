#
#
#
# numbers = 1
# while numbers <= 7:
#     print(numbers * "*")
#     numbers+=1
import math

name = input("Enter your name: ")
height = float(input("Enter your height(meters): "))
weight = float(input("Enter your weight(kilograms): "))
BMI = (weight/height)
if BMI <=18 :
    print("Hello " + name + " , your BMI is " + str(BMI) + ".You are underweight!")
elif BMI <=25:
    print("Hello " + name + " , your BMI is " + str(BMI) + ".You are normal")
elif BMI <=30:
    print("Hello " + name + " , your BMI is " + str(BMI) + ".You are overweight")
else:
    print("Hello " + name + " , your BMI is " + str(BMI) + ".You are obese.Sorry!")



