class Materia1:
    def __init__(self, name, teacher, topics) :
        self.name = name
        self.teacher = teacher
        self.topics = topics
        self.is_starting = False
    
    def star(self):
        self.is_starting = True
        print("Buenos días, la clase ha comenzado")

    def stop (self):
        self.is_starting = False
        print("La clase ha terminado")
    
    
    def change_teacher(self, new_teacher):
        self.teacher = new_teacher
        print(f"El profesor de {self.name} ahora es {self.teacher}.")
    
    def change_topics(self, new_topics):
        self.topics = new_topics
        print(f"El nuevo tema de la clase es {self.topics}")

clase1 = Materia1("Biologia", "Andre", "Animales")
print (clase1.name, clase1.teacher, clase1.topics)
clase1.star()
clase1.change_teacher("Luisa")
clase1.change_topics("Plantas")
clase1.stop()

class Extra(Materia1):
     def __init__(self, name,teacher,topics,dia_clase):
        super().__init__(name,teacher,topics)
        self.dia_clase=dia_clase

     def get_topics(self):
        return self.topics
    
     def set_topics(self, topics):
        self.topics = topics

     def get_dia_clase(self):
        return self.dia_clase
    
     def set_dia_clase(self, dia_clase):
        self.dia_clase = dia_clase

extra1 = Extra("Danza", "Andrea", "Salsa","miercoles")
print (extra1.name, extra1.teacher, extra1.topics,extra1.dia_clase)
extra1.set_dia_clase("jueves")
print(extra1.get_dia_clase())  
extra1.change_teacher("Luisa")
print(extra1.get_topics())

    