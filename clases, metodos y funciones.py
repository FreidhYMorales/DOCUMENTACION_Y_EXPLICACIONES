#FUNCIONES

#Existen dos tipos de funciones, la primera son funciones normales, donde definimos todos los procesos para realizar
#tareas complejas y la segunda son funciones lambda, que son funciones anónimas, es decir, no tienen nombre y realizan
#calculos simples ademas de que son utiles para no usar demasiadas lineas de código.

#Definir funciones normales
#Cuerpo de la función
# Palabra dedicada      le ponesmos un       Establecemos la 
# para definir          nombre a la          cantidad de parametros
# funciones             funcion             que requiere la funcion
#    |                       |                  |            |
#   \|/                     \|/                \|/          \|/
#   def             nombre_de_funcion      (parametro1, parametro2):
#EJEMPLO
def suma(x, y):
    return x + y
#Llamada a la función
print(suma(5, 7))

#funciones lambda
#Cuerpo de la función
#                                                               Establecemos los parametros     Establecemos lo que queremos que haga la funcion
#                                                                       |           |                |           |
#                                                                      \|/         \|/              \|/         \|/
#variables_contenedora_del_resultado_de_la_funcion_lambda = lambda parametro1, parametro2:      parametro1 + parametro2
#EJEMPLO
suma_de_dos_numeros = lambda x, y: x + y
print(suma_de_dos_numeros(5, 7))

#Cuando queramos crear una lista donde se almacenen los valores que cumpen con alguna funcion podemos utilizar la funcion
#filter, utiliza dos parametros, la primera es la funcion que queremos aplicar y la segunda es la lista que queremos recorrer
#para poder imprimir los valores que cumplan con la funcion, debemos convertir a una lista
#EJEMPLO
numeros = [1, 2, 3, 4, 5, 6]
#Aplicamos la funcion normal que solo nos muestr los numeros pares
def es_par(x):
    return x % 2 == 0 #La funcion develve un booleano si cumple o no
numeros_pares = filter(es_par, numeros) #la funcion filter sirve como bucle for donde pasa cada dato en la lista por la funcion
print(list(numeros_pares)) # [2, 4, 6]

#Tambien podemos utilizar funciones lambda para evitar crear un bloque de codigo, siempre y cuando sea simple
#Aplicamos la funcion lambda para que solo nos muestre los numeros pares
numeros_pares = filter(lambda x: x % 2 == 0, numeros)
print(list(numeros_pares)) # [2, 4, 6]



#PROGRAMACION ORIENTADA A OBJETOS

                #CLASES
                            #  Variable         
                            # Contenedora         tipo de        
                            # Del objeto           objeto      (PARAMETROS GENERALES DEL OBJETO)
                            #     |                  |               |         |         |
                            #    \|/                \|/             \|/       \|/       \|/
                            #   silla      =       silla         (*color,  *material, *tamaño)

#EJEMPLO
#la variable string es del tipo str, que contiene la cadena de caracteres "Cadena"
string = str("Cadena") 

                #Aqui la variable pertenece a una clase que tiene ciertos metodos o se pueden aplicar ciertas funciones
                            # VARIABLE  METODO    PARAMETROS DEL METODO
                            #   |          |               |
                            #  \|/        \|/             \|/
                            # auto    .arrancar  (*parametros_de_metodo)
#EJEMPLO
#a la variables string le aplico el metodo find para buscar una sub cadena, donde el parametro a buscar es "Cad"
string.find("Cad")

#los metodos son aplicables a a los objetos que sean del mismo tipo, ya que la forma de trabajar no es igual de una clase a otra
#las funciones son aplicables a cualquier tipo de objeto, ya que la forma de trabajar es igual para todos ya que su estructura son iguales
#en resumen los metodos son especificos y las funciones son generales
#EJEMPLO
"""
numero = 125
cadena = "PALABRAS"
print(dir(numero)) #aqui se imprimen todos los metodos que se pueden aplicar a la variable numero propia de los int 
print("\n\n")
print(dir(cadena)) #aqui se imprimen todos los metodos aplicables a la variable cadena propia de los str
"""

#CREACION DE CLASES EN PYTHON
#definimos una clase del tipo operacion
class Operacion:
    #definimos un inicializador que se llama a si misma en donde se pueden pasar dos parámetros para la propia clase 
    def __init__(self, operador1, operador2):
        self.operador1 = operador1
        self.operador2 = operador2
    def sumar(self):
        print(f"La suma es: {self.operador1 + self.operador2}")
    def restar(self):
        print(f"La resta es: {self.operador1 - self.operador2}")
    def multiplicar(self):
        print(f"La multiplicacion es: {self.operador1 * self.operador2}")
    def divicion(self):
        print(f"La division es: {self.operador1 / self.operador2}")
    def potencia(self):
        print(f"La potencia es: {self.operador1 ** self.operador2}")

#Pedir dos datos
numeros = list() #creamos una lista vacia

#Pedimos dos numeros
for i in range(2):
    numeros.append(int(input(f"ingrese el {i+1} numero: ")))

#variable opera que contiene dos parametros, el primero es para guardar el primer operador y el segundo para el segundo operador
opera = Operacion(*numeros)

#Aplicamos los metodos de la clase a la variable opera
opera.sumar()       #imprime la suma de dos numeros
opera.restar()      #imprime la resta de dos numeros
opera.multiplicar() #imprime la multiplicacion de dos numeros
opera.divicion()    #imprime la division de dos numeros
opera.potencia()    #imprime la potencia de dos numeros

class persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    def saludo(self):
        print(f"Hola mi nombre es {self.nombre} {self.apellido}!!")
        
nombre_completo = persona("Walter", "Figueroa")
nombre_completo.saludo() #imprime un saludo con el nombre y apellido de la persona 

nombre_completo = persona("Freid", "Morales")
nombre_completo.saludo() #imprime un saludo con el nombre y apellido de la persona 