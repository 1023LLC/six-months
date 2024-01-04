# def main():
#     name = get_name()
#     house = get_house()
#     print(f"{name} from {house}")
    
    
# def get_name():
#     return input("Name: ")


# def get_house():
#     return input("House: ")


# if __name__ == "__main__":
#     main()
    
    
    
# def main():
#     student = get_student()
#     print(f"{student[0]} from {student[1]}")
    
    
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return name, house


# if __name__ == "__main__":
#     main()


# def main():
#     student = get_student()
#     if student[0] == "Padma":
#         student[1] = "Ravenclaw"
#     print(f"{student[0]} from {student[1]}")
    
    
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return [name, house]


# if __name__ == "__main__":
#     main()


# def main():
#     student = get_student()
#     if student["name"] == "Padma":
#         student["house"] = "Ravenclaw"
#     print(f"{student["name"]} from {student["house"]}")
    
    
# def get_student():
#     return {"name": input("Name: "), "house" : input("house: ")}
    
# if __name__ == "__main__":
#     main()



# Using Classes

# class Student:
#     pass


# def main():
#     student = get_student()
#     if student.name == "Padma":
#         student.house = "Ravenclaw"
#     print(f"{student.name} from {student.house}")
    
    
# def get_student():
#     student = Student()
#     student.name = input("Name: ")
#     student.house = input("House: ")
#     return student
    
    
        
# if __name__ == "__main__":
#     main()







# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing Name!")
        
#         if house not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']:
#             raise ValueError("Invalid house!")
        
#         self.name = name
#         self.house = house


# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")
    
    
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
    
#     # try:
#     #     student = Student(name, house)
#     # except ValueError:
#     #     ...
    
#     student = Student(name, house)
#     return student
    
    
        
# if __name__ == "__main__":
#     main()


# How To Define your a __str__ function


# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing Name!")
        
#         if house not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']:
#             raise ValueError("Invalid house!")
        
#         self.name = name
#         self.house = house
        
#     def __str__(self):
#         return f"{self.name} from {self.house}"


# def main():
#     student = get_student()
#     print(student)
    
    
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     student = Student(name, house)
#     return student
    
    
        
# if __name__ == "__main__":
#     main()
    
    
    
# How to create your own Methods(functions) inside a class


# class Student:
#     def __init__(self, name, house, patronus):
#         if not name:
#             raise ValueError("Missing Name!")
        
#         if house not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']:
#             raise ValueError("Invalid house!")
        
#         self.name = name
#         self.house = house
#         self.patronus = patronus
        
        
#     def __str__(self):
#         return f"{self.name} from {self.house}"
    
    
#     def charm(self):
#         match self.patronus:
#             case 'stag':
#                 return '🐴'
#             case 'otter':
#                 return '🦦'
#             case 'Jack Russell Terrier':
#                 return '🐶'
#             case _:
#                 return '💀'


# def main():
#     student = get_student()
#     print("Expecto Patronum!")
#     print(student.charm())
        
    
# def get_student():
#     name = input("Name: ")
#     house = input("House: ") 
#     patronus = input("Patronus: ")
#     student = Student(name, house, patronus)
#     return student
    
    
        
# if __name__ == "__main__":
#     main()



# Using Decorators


# class Student:
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house
        
        
#     def __str__(self):
#         return f"{self.name} from {self.house}"
    
    
#     @property
#     def name(self):
#         return self._name
    
    
#     @name.setter
#     def name(self, name):
#         if not name:
#             raise ValueError("Missing Name!!")
#         self._name = name
    
    
    
#     # Getter
#     @property
#     def house(self):
#         return self._house
    
#     # Setter
#     @house.setter
#     def house(self, house):
#         if house not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']:
#             raise ValueError("Invalid house")
#         self._house = house
    
    

# def main():
#     student = get_student()
#     # student.house = "Number Four, Privet Drive"
#     print(student)
        
    
# def get_student():
#     name = input("Name: ")
#     house = input("House: ") 
#     student = Student(name, house)
#     return student
    
    
        
# if __name__ == "__main__":
#     main()




# Using Classmethods(PART: ONE)

# import random


# class Hat:
#     def __init__(self):
#         self.houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
    
    
    
#     def sort(self, name):
#         house = random.choice(self.houses)
#         print(name, "is in", house)
    



# hat = Hat()
# hat.sort("Harry")



# Using Classmethods(PART: TWO)


# import random


# class Hat:
    
#     houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
    
    
#     @classmethod
#     def sort(cls, name):
#         house = random.choice(cls.houses)
#         print(name, "is in", house)
    


# Hat.sort("Harry")



# Cleaning Up Our initial Bad Code Design using Classmethod and removing redundant function

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
        
    

        
# if __name__ == "__main__":
#     main()




# Class Inheritance



# class Wizard:
#     def __init__(self, name):
#         if not name:
#             raise ValueError("Missing Name!!")
#         self.name = name




# class Student(Wizard):
#     def __init__(self, name, house):
#         super().__init__(name)
#         self.house = house
        
        
        

# class Professor(Wizard):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject
        
        
        
# wizard = Wizard('Albus')
# student = Student('Harry', 'Gryffindor')
# professor = Professor('Severus', 'Defense Against the Dark Arts')




# Operator Overloading


class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        
        
    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickels, {self.knuts} Knuts"
    
    
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)
        
        
potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)


total = potter + weasley
print(total)