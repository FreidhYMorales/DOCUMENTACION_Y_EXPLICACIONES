import statistics
import os

'''
Para definir funciones se usa la siguiente estructura:

def nombre_de_la_funcion(parametro1, parametro2, ...):
    ###
       
       Aqui se asignan los procesos o pasos a seguir
       siguiento las tabulaciones para cada orden que se le de
       
    ###
    return x // Aqui retornamos los valores que procesamos

miNombre = "Freidh"
cantidad_veces = 5

def imprimir_nombre(nombre):
    print((nombre + "\n") * 5)
    
imprimir_nombre(miNombre)

def imprimir_nveces(cadena, nveces):
    for i in range(nveces):
        print(cadena)
        
oracion = str(input("Cadena a imprimir: "))
num_veces = int(input("Ingrese la cantidad de veces: "))

imprimir_nveces(oracion, num_veces)


lista_num = [1 , 2 , 3 , 4, 5]

def sum_lista_datos(lista):
    sumn = 0
    for i in lista:
        sumn += i
    print(f"Suma de la lista de datos: {sumn}")
    print(f"Suma de la lista: {sum(lista)}")

def prom_lista_datos(lista):
    '''
"""sumT = 0
    nTotal = len(lista)
    for i in lista:
        sumT += i
    prom = sumT / nTotal
    print(f"Promedio de la lista: {prom}")
    """'''
    print(f"El promedio es: {(sum(lista))/(len(lista))}")
    print(f"El promedio es: {statistics.mean(lista)}")
        
def prom_num_pares(lista):
    sumTpares = 0
    tPares = 0
    for i in lista:
        if i % 2 == 0:
            sumTpares += i
            tPares += 1
    print(f"Total promedio pares: {sumTpares/tPares}")

sum_lista_datos(lista_num)
prom_lista_datos(lista_num)    
prom_num_pares(lista_num)

lista_cadenas = ["Freidh", "Yannel", "Morales", "Gonzalez"]

def sum_cantidad_letras_de_cadenas(lista):
    sumLetras = 0
    for i in lista:
        sumLetras += len(i)
    print(f"Suma de las letras de cada cadena: {sumLetras}")
    
sum_cantidad_letras_de_cadenas(lista_cadenas)

num1 = -3
num2 = -2

def num_mayor(x, y):
    if x > y:
        print(f"El numero mayor es: {x}")
    elif y > x:
        print(f"El numero mayor es: {y}")

num_mayor(num1, num2)

def tabla_multiplicacion(num):
    for i in range(1, 11):
#        print('{} * {:>2} = {}'.format(num, i, (i * num)))
        print(f"{num} * {i:>2} = {(i * num)}")
        
numero = int(input("Ingrese el numero que desee imprimir la tabla de multiplicar: "))
tabla_multiplicacion(numero)

def terminacion_4(num):
        numT = str(num)
        
        if numT.endswith('4'):      
            print("El ultimo digito del numero ingresado es 4!!")
        else:
            print("El ultimo digito del numero ingresado no es 4!!")
            
numero = 4
terminacion_4(numero)
'''
def terminacion_4(num):
    canFin = 0
    
    for i in num:
        numT = str(i)
        if numT.endswith('4'):      
            canFin += 1
                    
    print(f"La cantidad de digitos finalizados en 4 son: {canFin}")
            
numero = [4, 14, 5, 3, -124, 0]
terminacion_4(numero)

input()
os.system("cls")