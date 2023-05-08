class Text:
    def __init__(self, name, paginas, autor, publicacion) :
        self.name = name
        self.paginas = paginas
        self.autor = autor
        self.publicacion = publicacion
    
    def change_paginas(self, new_paginas):
        self.paginas= new_paginas
        print(f" {self.name} ahora tiene {self.paginas} paginas.")
    
    def change_publicacion(self,new_publicacion):
        self.publicacion = new_publicacion
        print(f"{self.name} ahora será publicado {self.publicacion}.")


texto1 = Text("La historia del amor","222", "Juan Sasvedra", "02 de abril de 2018")
texto1.change_paginas("204")
class Books(Text):
    def __init__(self, name,paginas,autor,publicacion,genero):
        super().__init__(name,paginas, autor, publicacion)
        self.genero=genero
    def get_paginas(self):
        return self.paginas
    
    def set_paginas(self, paginas):
        self.paginas = paginas

    def get_genero(self):
        return self.genero
    
    def set_genero(self, genero):
        self.genero = genero
    def change_genero(self,new_genero):
        self.genero = new_genero
        print(f"{self.name} en realidad es un libro de {self.genero}.")
libro1=Books("Despues","256", "Stephen King","2020","suspenso")
libro1.set_paginas("223")
print(libro1.get_paginas())
libro1.change_genero("Terror")
