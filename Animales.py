class Animals:
    def __init__(self, name, alimentacion, patas, reproduccion):
        self.name = name
        self.alimentacion = alimentacion
        self.patas = patas
        self.reproduccion =reproduccion
        self.is_running = False


    def run(self):
        self.is_running = True
        print("El animal esta corriendo")
    
    def stop_run(self):
        self.is_running = False
        print("El animal se ha detenido")
    
    def get_patas(self):
        return self._patas
    
    def set_patas(self, patas):
        self._patas = patas

animal1=Animals("Perro","Carnivoro","4", "mamifero")
print(animal1.name,animal1.alimentacion)
animal2=Animals("Araña", "Carnivoro", "8","oviparo")
animal1.run()
animal2.set_patas(6)
print(animal2.get_patas())  

class Aves(Animals):
     def __init__(self, name, alimentacion, patas, reproduccion):
        super().__init__(name,alimentacion,patas,reproduccion)

     def run(self):
        self.is_running = True
        print(f"El {self.name} esta volando")
    
     def stop_run(self):
        self.is_running = False
        print(f"El {self.name} ha aterrizado")
ave1=Aves("Aguila","carnivora","2", "por huevos")
ave1.run()
ave1.stop_run()