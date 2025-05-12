import os
cadena = "Conjunto De Caracteres" 
os.system("cls")

#Fucniones o metodos integrados de cadenas de texto
#dir(), devuelve todas las funciones disponibles dependiendo del tipo de variable que se ponga en los parentesis
print(dir(dict())) #imprime en consola toda las funciones disponibles para la variable
input()
os.system("cls")

#METODOS PARA CARACTERES DE CADENAS
#str.upper(), pone en mayusculas todos los caracteres de la variable tipo cadena que se ponga dentro
print("Texto en MAYUSCULAS: " + cadena.upper())
#str.lower(), pone en minuscula todo los caracteres de una cadena
print("Tesxto en minusculas: " + cadena.lower())
#str.capitalize(), pone la primera letra en mayuscula luego todo se queda en minuscula
print("Primera letra Mayuscula: " + cadena.capitalize() + "\n")

#METODOS PARA ENCONTRAR VALORES DE CADENAS
#str.find("valor_busqueda"), metodo para encontrar una subcadena de una cadena
valor_busqueda_find = "Caracter"
print(f"Posicion: {cadena.find(valor_busqueda_find)}") #Devuelve la posicion donde empieza la subcadena, toma en cuanta mayusculas y minusculas

valor_busqueda_find = "Metodo"
print(f"Posicion: {cadena.find(valor_busqueda_find)}")#Devuelve -1 cuando no se encuentra al valor

#str.index("valor_busqueda"), metodo para encontrar una subcadena de una cadena
valor_busqueda_index = "Caracter"
print(f"Posicion: {cadena.index(valor_busqueda_index)}") #Devuelve la posicion donde empieza la subcadena, toma en cuanta mayusculas y minusculas

valor_busqueda_index = "Metodo"
#print(f"Posicion: {cadena.index(valor_busqueda_index)}") #Devuelve una excepcion o error y para el programa
input()
os.system("cls")

#METODOS PARA VERIFICAR TIPO DE CADENA
#str.isalpha(), revisa si toda la cadena es de letras, si tiene espacion devuelve False por defecto
print(f"Tipo de cadena alfabetica: {cadena.isalpha()}") #Devuleve un booleano False si no es completamente alfabetica

cadena = "palabra"
print(f"Tipo de cadena alfabetica: {cadena.isalpha()} \n") #Devuleve un booleano True si es completamente alfabetica

#str.isnumeric(), revisa si toda la cadena de carcateres es numerica
print(f"Tipo de cadena numerica: {cadena.isnumeric()}") #Devuleve un booleano False si no es completamente numerica

cadena = "1234567890"
print(f"Tipo de cadena numerica: {cadena.isnumeric()} \n") #Devuleve un booleano True si es completamente numerica

#str.isalnum(), revisa si toda la cadena es alfanumerica, si tiene espacios o caracteres especiales devuelve False por defecto
cadena = "Cadena @lfaNum3ric@"
print(f"Tipo de cadena alfanumerica: {cadena.isalnum()}") #Devuelve un boolenao False si no es alfanumerica

cadena = "Cad3nalfanum3r1ca"
print(f"Tipo de cadena alfanumerica: {cadena.isalnum()}") #Devuelve un boolenao True si es alfanumerica 
#devuelve true sin importar si todos los caracteres son de un solo tipo

input()
os.system("cls")

#METODOS PARA IDENTIFICAR VALORES
cadena = "Cadena"
#str.startswith(valor_busqueda), identifica si el primer valor coincide con el valor de busqueda
print(f"La cadena empieza con A: {cadena.startswith("A")}") #Devuelve un booleano False si no coinciden
print(f"La cadena empieza con C: {cadena.startswith("C")}") #Devuelve un booleano True si coinciden

#str.endswith(valor_busqueda), identifica si el ultimo valor coincide con el valor de busqueda
print(f"La cadena termina con c: {cadena.endswith("c")}") #Devuelve un booleano False si no coinciden
print(f"La cadena termina con a: {cadena.endswith("a")} \n") #Devuelve un booleano True si coinciden

#METODOS DE CONTEO
#str.count(valor_busqueda), devuelve un valor de las insidencias o valores que coinciden con el valor de busqueda
cadena = [1, 2, 3, 1, 3, 1, 4, "a", "b", "c", "a", "z", "a", "a"] #Funciona con listas, tuplas y conjuntos

contador = cadena.count(1)
print(f"Cantidad de veces que se repite el 1: {contador}")

contador = cadena.count("a")
print(f"Cantidad de veces que se repite la 'a': {contador}")

#len(), sirve para ver la cantidad de datos o caracteres de una cadena, funciona con listas, tuplas y conjuntos
print(f"Cantidad de datos dentro de la cadena: {len(cadena)} \n")

#METODOS DE CORRECCION DE CADENAS DE CARACTERES
#str.replace(valor_a_remplazar, valor_para_reemplazar), reemplaza una cadena de carcateres por otra,
#el primer parametro es el valor que queremos reemplazar,
#el segundo parametro es el valor por el cual queremos reemplazarlo
cadena = "Cadena de Texto"
print(f"Palabra reemplazada: {cadena.replace("Texto", "Caracteres")}")

#str.split(valor_de_separacion), separa una cadena por partes, segun el valor de separacion
print(f"Cadena separada y convertida en lista: {cadena.split(" ")}") #el espacio es el valor de separacion, cada vez que lo encuentre
#separa la cadena por partes
input()
os.system("cls")

#Funciones y metodos para listas
lista = list() #crear una lista en blanco
print(f"Datos en lista: {lista}")

#list.append(valor_para_agregar_a_la_lista), sirve para agregar un valor a una lista
lista.append(1)
lista.append(3)
lista.append(2)
lista.append("b")
lista.append("a")
lista.append("c")

print(f"Datos en lista: {lista}")

#list.insert(indice_de_lugar_para_agregar_un_valor_a_la_lista, valor_para guardar_en_esa_pocision), sirve para agregar datos
#a una lista en un lugar especifico
lista.insert(3, 4)
lista.insert(-1, "d") #los indices negativos sirven para agragar en posiciones finales, en este caso es en la posicion penultima

print(f"Datos en lista: {lista}")

#list.extend([lista]), agrega una lista a otra lista en las ultimas posiciones
lista.extend([True, False, "a", "b", "c", 1, 3, 6, 1])

print(f"Datos en lista: {lista}")

#list.pop(valor_de_indice), elimina el valor de una lista segun el indice
lista.pop(1) #elimina el segundo valor de la lista por indice, por defecto elimina el ultimo valor (-1)
lista.pop(-2) #soporta numeros negativos para ir a las ultimas posiciones, en este caso la penultima

print(f"Datos en lista: {lista}")

#list.remove(valor_de_busqueda_para_eliminar), elimina el valor de una lista segun el valor de busqueda, no necesita indice,
#y solo lo hace una vez
lista.remove("a")
lista.remove(1)

print(f"Datos en lista: {lista}")

#list.clear(), elimina todos los datos de una lista
lista.clear()

print(f"Datos en lista: {lista}")

lista.extend([9, 2, 3, 5, 6, 8, 5, 0])

print(f"Datos en lista: {lista}")

#list.reverse(), solo invierte el orden ya establecido de una lista
lista.reverse()

print(f"Datos en lista: {lista}")

#list.sort(), ordena de mayor a menor una lista, la lista solo puede ser de un tipo, solo de numeros o solo de caracteres
lista.sort()

print(f"Datos en lista: {lista}")

lista.sort(reverse= True) #si utilizamos el parametro reverse= True, el orden se invierte, en este caso de menor a mayor

print(f"Datos en lista: {lista}")

