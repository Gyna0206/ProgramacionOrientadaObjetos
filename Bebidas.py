class Drink:
    def __init__(self, name, tamaño, marca,tempe) :
        self.name = name
        self.tamaño = tamaño
        self.topics = marca
        self.tempe = tempe    
    
    def change_tamaño(self, new_tamaño):
        self.tamaño = new_tamaño
        print(f"La {self.name} ahora es {self.tamaño}.")
    
    def change_tempe(self,new_tempe):
        self.tempe = new_tempe
        print(f"Ahora la bebida es {self.tempe}")

bebida1 = Drink("Cafe", "Pequeño", "Sello rojo","Frio")
print (bebida1.name, bebida1.tamaño, bebida1.tempe)
bebida1.change_tempe("Caliente")
class Coctels(Drink):
    def __init__(self, name,tamaño,marca, tempe,contenido_alcohol,tipo):
        super().__init__(name,tamaño, marca, tempe)
        self.contenido_alcohol=contenido_alcohol
        self.tipo=tipo
    def get_contenido_alcohol(self):
        return self.contenido_alcohol
    
    def set_contenido_alcohol(self, contenido_alcohol):
        self.contenido_alcohol = contenido_alcohol

    def get_tipo(self):
        return self.tipo
    
    def set_tipo(self, tipo):
        self.tipo = tipo
coctel1=Coctels("Cerveza","350ml","Club Colombia","Fria","5%","Negra")
coctel1.change_tamaño("litro")
coctel1.set_tipo("Dorada")
print(coctel1.get_tipo())
print(coctel1.get_contenido_alcohol())
