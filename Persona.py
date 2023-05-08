class Person:
    def __init__(self, name, age, profession,activities):
        self.name = name
        self.age = age
        self.profession = profession
        self.activities = activities
        self.is_presenting = False
    
    def greet(self):
        self.is_presenting = True
        print("Buenos días, solecitos")

    def introduce (self):
        self.is_presenting =True
        print(f"Hola, mi nombre es {self.name}, tengo {self.age} años, soy {self.profession}")
    
    
    def change_profession(self, new_profession):
        self.profession = new_profession
        print(f"La persona ahora es {self.profession}.")
    
    def change_activities(self, new_activities):
        self.activities = new_activities
        print(f"La persona esta {self.activities}")


person1 = Person("David","28","Politologo","Trabajando")
print (person1.name, person1.age, person1.profession, person1.activities)

person1.introduce()
person1.change_activities("Durmiendo")

class Estudiante(Person):
    def __init__(self, name, age, profession,activities,university):
        super().__init__(name,age,profession,activities)
        self.university=university

    def change_university(self, new_university):
        self.university=new_university
        print(f"{self.name} ahora estudia en {self.university}")
    def introduce (self):
        self.is_presenting =True
        print (f"Hola, mi nombre es {self.name}, tengo {self.age} años, estudio para ser {self.profession} en la universidad {self.university}")
    

estudiante1 = Estudiante("Julian","22","medico","estudiando","Nacional")
estudiante1.introduce()
estudiante1.change_university("El Bosque")
estudiante1.introduce()