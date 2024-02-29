# first_no = int(input("Enter your first number: "))
# second_no = int(input("Enter your second number: "))
# multiply = first_no * second_no
# print(multiply)
#
#
# m_list = [54,44,27,79,91,41]
# print(m_list)
# m_pop = m_list.pop(4)
# print(m_list)
# print(m_pop)
# m_list[1] = int(m_pop)
# m_list.append(int(m_pop))
# print(m_list)
# m_list.append([1,int(m_pop)])
# print(m_list)
# m_list.insert(3,450)
# print(m_list)
#
# # #
# sample_dist = {'a':100,'b':200,'c':300,'d':400}
# print(sample_dist)
# print(sample_dist.items())
# print(sample_dist.get('b'))
# sample_dist['e'] = '500'
# print(sample_dist)
# sample_dist.update({'a':250,'b':350})
# print(sample_dist)
#
# if 200 in sample_dist.values():
#     print("Perfect")
# else:
#     print("Hmmm!Something is wrong")
#
#
# for key in sample_dist:
#     print(key)
# for key,values in sample_dist.items():
#     print(key,values)
#
# for key in sample_dist:
#     name = input("Enter your name: ")
#     adm_no  = input("Enter your adm no: ")
#     form = input("Enter your form: ")
#     math:str = input("Enter your Maths mark: ")
#     eng = input("Enter your English mark: ")
#     if int(math) > 10:
#         sum =int(math)+ int(eng)
#         print(sum)
#         if sum>20:
#             print("Hello " + name, " you have passed your test!")
#
#     else:
#         sum = int(math) + int(eng)
#         print(sum)
#         if sum < 20:
#             print("Hello " + name, " you have failed your test!Please do corretions..")
#
# answer = "2 months"
# max_attempts = 3
# attempts = 3
# count = 1
# while count <= max_attempts:
#     count = count + 1
#     print("How long did it take chatGPT to get to 100 million users?")
#     ans = input("")
#     if ans != answer:
#         attempts = attempts - 1
#         if attempts == 0:
#             print("You are out of attempts! Please try again later.")
#         elif attempts == 1:
#             print("Wrong! You have 1  attempt to go ")
#         else:
#             print("Wrong! You have " + str(attempts) + "  attempts to go ")
#     else:
#         print("Correct! You are a champion")

#
# try:
#     num = int(input("Enter your number: "))
#     print(num)
# except ValueError:
#     print("Invalid input!")

# def translate(phrase):
#     translation = ""
#     for letter in translation:
#         if letter in "AEIOUaeiou":
#             translation = translation + "g"
#         else:
#             translation = translation + letter
#     return translation
#
# print(translate(input("Enter your phrase: ")))



# # sets
# s = set([1,2,3,4])
# print(s)
# s.add(6)
# print(s)

# # funtions trial
# def say_hi(name, age, institution):
#     print("Hello " + name + " you are " + age + " and have a honors degree from " + institution)
# say_hi("William","18","Stanford University")

class mychild:
    def __init__(self,firstname,lastname,age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    def __str__(self):
        return f"{self.firstname}{self.age}"
Robi = mychild("Yvonne","Robi",18)
print(f"God says:{Robi.firstname} {Robi.lastname}, you are {Robi.age} and  I know the number of hairs on your head.Worry not for I know the plans I have for you,plan to prosper you and not to harm you, plans to give you a hope and a future.")





