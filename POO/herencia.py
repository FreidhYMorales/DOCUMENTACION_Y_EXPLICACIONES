#HERENCIA DE CLASES
#La herencia permite pasar codigo de una clase a otra y poder reutilizarlo sin la necesidad de reescribirlo en su totalidad
#Se pueden heredar mas de una clase 
import os
os.system("cls")
class Animal:
    #Metodo dedicado a construir el objetos, conocido mas como "Constructores"
    def __init__(self, nombre, dueno):
        self.nombre = nombre
        self.dueno = dueno
    def Sonido(self):
        return "Sonido del Animal"
    #Metodo dedicado para retornar una cade de texto cuado se llama al objeto
    def __str__(self):
        return f"{self.nombre} {self.dueno} {type(self).__name__}"
    
class Mamiferos:
    tipo = "Mamifero"
    
class Perro(Animal, Mamiferos):
    def __init__(self, nombre, dueno, color, raza):
        super().__init__(nombre, dueno)
        self.color = color
        self.raza = raza
        self.tipo = Mamiferos.tipo
    def Sonido(self):
        return "Guau"

perro1 = Perro("Doggy", "Emaboy", "Blanco", "French")
print(f"El {type(perro1).__name__} hace: {perro1.Sonido()}")
print(perro1)