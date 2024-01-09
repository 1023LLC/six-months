# def main():
#     student = get_student()
#     print(f"{student['name']} from {student['house']}")


# def get_student():
#     return {'name': input("Name: "), 'house': input("House: ")}


# main()



# CLASSES




# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing Name!")
#         self.name = name
        
#         if house not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']:
#             raise ValueError("Invalid house!")
#         self.house = house


# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
    
#     return Student(name, house)


# main()





# TRY AND EXCEPT BLOCK


# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing Name!")
#         self.name = name
        
#         if house not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']:
#             raise ValueError("Invalid house!")
#         self.house = house


# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")


# def get_student():

#     try:
#         name = input("Name: ")
#         house = input("House: ")

#         return Student(name, house)
#     except ValueError as e:
#         print(f"Error: {e}")
        

# main()



# CREATING OUR OWN FUNCTIONS


# class Student:
#     def __init__(self, name, house, patronus):
#         if not name:
#             raise ValueError("Missing Name!")
#         self.name = name
        
#         if house not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']:
#             raise ValueError("Invalid house!")
#         self.house = house
#         self.patronus = patronus
        
#     def __str__(self):
#         return f"{self.name} from {self.house}"
    
#     def charm(self):
#         match self.patronus:
#             case 'Stag':
#                 return '*%*'
    
        


# def main():
#     student = get_student()
#     print(student)
#     print("Expecto Patronum!!")
#     print(student.charm())


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     patronus = input("Patronus: ")
    
#     return Student(name, house, patronus)


# main()




# class Student:
#     def __init__(self, name, house):
        
#         self.name = name
#         self.house = house

        
        
#     def __str__(self):
#         return f"{self.name} from {self.house}"
    
    
#     @property
#     def house(self):
#         return self._house
        
#     @house.setter   
#     def house(self, house):
#         if house not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']:
#             raise ValueError("Invalid house!")
#         self._house = house


#     @property
#     def name(self):
#         return self.name
    
#     @name.setter
#     def name(self, name):
#         if not name:
#             raise ValueError("Missing Name!")
        

# def main():
#     student = get_student()
#     print(student)

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
    
#     return Student(name, house)


# main()




# CLASSMETHODS


# import random

# class Hat:
#     def __init__(self):
#         self.houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
    
    
#     def sort(self, name):
#         house = random.choice(self.houses)
#         print(name, "is in", house)
    
    
    
# hat = Hat()
# hat.sort("Harry")


# import random

# class Hat:
#     houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
    
#     @classmethod
#     def sort(cls, name):
#         house = random.choice(cls.houses)
#         print(name, "is in", house)
    
    
    
# Hat.sort("Harry")


# import random

# def main():
#     hat = sort("Harry")


# def sort(name):
#     houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
#     print(name, "is in", random.choice(houses))


# main()




# class Student:
#     def __init__(self, name, house):
        
#         self.name = name
#         self.house = house

        
        
#     def __str__(self):
#         return f"{self.name} from {self.house}"
    
#     @classmethod
#     def get(cls):
#         name = input("Name: ")
#         house = input("House: ")
        
#         return cls(name, house)
    
        

# def main():
#     student = Student.get()
#     print(student)


# main()





# INHERITANCE



# class Wizard:
#     def __init__(self, name):
#         if not name:
#             raise ValueError("Missing Name!!")
#         self.name = name

#     def __str__(self):
#         return f"{self.__class__.__name__}: {self.name}"


# class Student(Wizard):
#     def __init__(self, name, house):
#         super().__init__(name)
#         self.house = house

#     def __str__(self):
#         return f"{super().__str__()}, House: {self.house}"


# class Professor(Wizard):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject

#     def __str__(self):
#         return f"{super().__str__()}, Subject: {self.subject}"


# wizard = Wizard("Albus")
# student = Student("Harry", "Gryffindor")
# professor = Professor("Severus", "Defense Against the Dark Arts")

# print(wizard)
# print(student)
# print(professor)



# OPERATOR OVERLOADING


# class Vault:
#     def __init__(self, galleons=0, sickles=0, knuts=0):
#         self.galleons = galleons
#         self.sickles = sickles
#         self.knuts = knuts
        
#     def __str__(self):
#         return f"{self.galleons} galleons, {self.sickles} sickels, {self.knuts} knuts"
        
# potter = Vault(100, 50, 25)

# print(potter)


# weasley = Vault(25, 50, 100)

# print(weasley)

# galleons = potter.galleons + weasley.galleons
# sickles = potter.sickles + weasley.sickles
# knuts = potter.knuts + weasley.knuts

# total = Vault(galleons, sickles, knuts)
# print(total)






class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        
    def __str__(self):
        return f"{self.galleons} galleons, {self.sickles} sickels, {self.knuts} knuts"

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)


potter = Vault(100, 50, 25)

weasley = Vault(25, 50, 100)


print(potter + weasley)



