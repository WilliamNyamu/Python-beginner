class Employees:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
class Receptionist(Employees):
    def __init__(self,name,salary,gender):
        super().__init__(name,salary)
        self.gender = gender
class Front_end_developer(Employees):
    def __init__(self,name,salary,lang):
        super().__init__(name,salary)
        self.lang = lang

obj1 = Receptionist("Suzanne","$560","Female")
obj2 =Employees("Felix",1000000)
obj3 = Front_end_developer("William","$130,000","html,css,JavaScript")
print(obj1.name)
print(obj2.salary)
print(f"ChatGPT: Here is a seasoned front-end web developer I would recommend for your project: {obj3.name}, he earns a net salary of {obj3.salary} per year and is competent at {obj3.lang}")
# print(obj3.lang)


