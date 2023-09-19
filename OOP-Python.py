from datetime import date

# class
class Student:
    # class attributes
    no_of_stf = 0

    # initialization function that run when create object of class
    # parameter should be assigned in object
    # self for assgin parameter values to its self
    # we can implement encapculation princple by private attriute and getters and setters
    # instance methods task self as parameter
    def __init__(self, name, age, courses):
        # add self.__attribute to make it privte instead of public
        self.__name = name
        self.__age = age
        self.__courses = courses
        # increate by 1 when object created
        Student.no_of_stf += 1

    # getter  and setters
    def get_name(self):
        return self.__name

    def set_name(self, newName):
        self.__name = newName

    def get_age(self):
        return self.__age

    def set_age(self, newAge):
        self.__age = newAge

    def get_courses(self):
        return self.__courses

    def set_courses(self, newCourses):
        self.__courses = newCourses

    # instance methods task self as parameter
    def describe(self):
        print(f"my name is {self.name} at {self.age}. I study {self.courses}")

    def isOld(self, num):
        if self.age >= num:
            print("Student is Old")
        else:
            print("Studen is Young")


student_1 = Student("Ahmed", 20, ["cs", "math"])
student_2 = Student("Oamr", 30, ["cs", "math"])
student_3 = Student("Fahmy", 50, ["cs", "math"])

print(student_3.get_age())
print(student_3.set_age(15))
print(student_3.get_age())

class Pizza:
    def __init__(self, ingrediants):
        self.ingrediants =ingrediants

    @classmethod
    def veg(cls):
        return cls({"mashrooms","olives","onions"})
    
    @classmethod
    def  margherita(cls):
        return cls({"mozarella","suaze"})
    
    # dunder funtion "di - underscore" in start and end of function name
    def __str__(self):
        return f"pizza ingredients are {self.ingrediants}"
    
pizza_1 = Pizza({"tomato","olives"})
pizza_2 = Pizza.veg()
pizza_3 = Pizza.margherita()

print(pizza_1)
print(pizza_2)
print(pizza_3)


# static meathods make huge functionlity in code like below example
class Calc:
    @staticmethod
    def add(num_1, num_2):
        return num_1 + num_2
    
    @staticmethod
    def substract(num_1, num_2):
        return num_1 - num_2
    
    @staticmethod
    def multi(num_1, num_2):
        return num_1 * num_2
    
    @staticmethod
    def divide(num_1, num_2):
        return num_1 / num_2
    
print(Calc.add(5,10))
print(Calc.substract(5,10))
print(Calc.multi(5,10))
print(Calc.divide(5,10))