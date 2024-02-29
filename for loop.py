number = [234,768,987,5677,5667]
for i in number:
    print(i)

set = {'John','Mary','Smith','Jane'}
for name in set:
    print(name)


my_string = "Hello World, welcome to my channel"
for letter in my_string:
    print(my_string)

char = ('a','b','c','d')
for letter in char:
    if letter =='b':
        continue
    print(letter)
else:
    print("finished")