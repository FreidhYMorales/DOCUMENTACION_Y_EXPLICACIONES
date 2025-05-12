#ciclos for

#for nombre_varible in range(dato_de_inicio, dato_de_finalizacion, de_cuanto_en_cuanto_pasar_cada_dato):
animales = ["Oso", "Gato", "Perro", "Aguila", "Pez"]

#Por cada animal en la lista animales los va a imprimir en consola
for animal in animales:
    print(animal)

#range(primer_parametro, segundo_parametro, tercer_parametro)
#range(primer_parametro), este tiene dos funciones, el primero es la cantidad de veces que queremos iterar

#Por cada numero hasta que sean 10, o sea del 0 al 9
for numero in range(10):
    print(numero)
#range(primer_paramtro, segundo_parametro), aqui el primer parametro funciona como el dato de inicio,
#y el segundo parametro es el dato donde queremos terminar

#Por cada numero en el rango de x >= 1 y x < 10, o sea del 1 al 9
for numero in range(1, 10):
    print(numero)
    
#Cuando queramos llegar al dato exacto es mejor establecer un numero despues del que queremos que termine
for numero in range(1, 11):
    print(numero)#datos del 1 al 10
    
#range(primer_paramtro, segundo_parametro, tercer_parametro), aqui el primer parametro funciona como el dato de inicio,
#el segundo parametro es el dato donde queremos terminar y el tercer parametro es de cuanto en cuato queremos pasar los dtos o numeros 
    
#Por cada nuemro par hasta el 20    
for par in range(2, 21, 2):
    print(par)