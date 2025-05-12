#PROGRAMACION ORIENTADA A OBJETOS
#METODOS Y ATRIBUTOS
import os
os.system("cls")

#Los Atributos de Instancia son propios del objeto y se definen cuando se crea y los atributos de clase son propias de la clase en general y no son modificables, pero si accesibles
class Operaciones:
    def __init__(self, numero1, numero2):
        #Atributos de Instancia
        self.num1 = numero1
        self.num2 = numero2
    #Metodos de Instancia // Son metodos aplicables a un objeto creado, no se pueden utilizar sin haber creado el objeto en primer lugar.
    def Suma(self):
        return self.num1 + self.num2
    def Resta(self):
        return self.num1 - self.num2
    def Multiplicacion(self):
        return self.num1 * self.num2
    def Division(self):
        return self.num1 / self.num2
    
numero = Operaciones(10, 5)
print(f"La suma de los numeros es: {numero.Suma()}")
print(f"La resta de los numeros es: {numero.Resta()}")
print(f"La multiplicacion de los numeros es: {numero.Multiplicacion()}")
print(f"La division de los numeros es: {numero.Division()}")

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print(" ")
class Circulo:
    #Atributo de Clase
    pi = 3.14159
    def __init__(self, radio):
        #Atributos de Instancia
        self.radio = radio
    #Metodos de instancia
    def Area(self):
        return Circulo.pi * (self.radio * 2)
    #Metodos de Clase // Estas pertenecen a la propia clase y tiene acceso a la misma sin la necesidad de tener un dato de instnacia
    #Se define primero con @classmethod y luego se define el metodo
    @classmethod
    #El "cls" se pone como atributo de metodo sustituyendo el "self" de los metodos de instancia
    def DesdeDiametro(cls, diametro):
        #Utiliza un dato independienta al objeto para definirse a si misma, en este caso la clase requiere el atributo radio para crearse
        #y se utiliza el diametro para definir el dato requerido como altenrativa para crear el objeto
        radio = diametro / 2 
        #en este caso se utiliza el cls() para acceder a los atributos de clase
        return cls(radio)
    
#Creando obejto y utilizando metodos de insancia    
circulo1 = Circulo(5)
print(f"Area del circulo con radio 5: {circulo1.Area()}")

#Creando el objeto usando metodos de clase
circulo2 = Circulo.DesdeDiametro(10)
print(f"Area del circulo con diametro 10: {circulo2.Area()}")
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print(" ")
class Numero:
    #Metodos Estaticos
    #Los metodos estaticos no requieren del uso de los atributos de instancia del objeto, se pueden utilizar de forma independiente a estas
    #Se Definen con el encabezado @staticmethod y luego se definen como una funcion normal, sin utilizar los valores de instancia, esto se repite para cada metodo estatico
    @staticmethod
    def Suma(num1, num2):
        return num1 + num2
    @staticmethod
    def Resta(num1, num2):
        return num1 - num2
    @staticmethod
    def Multiplicacion(num1, num2):
        return num1 * num2
    @staticmethod
    def Division(num1, num2):
        return num1 / num2
    
numero = Numero()
#Utilizando metodos estaticos
print(f"La suma de los numeros 2 y 3: {numero.Suma(2, 3)}")
print(f"La resta de los numeros 2 y 3: {numero.Resta(2, 3)}")
print(f"La multiplicacion de los numeros 2 y 3: {numero.Multiplicacion(2, 3)}")
print(f"La division de los numeros 2 y 3: {numero.Division(2, 3)}")