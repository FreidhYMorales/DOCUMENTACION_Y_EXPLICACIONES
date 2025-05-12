#ciclos while

booleano = True
numero = 1

while numero > 10:
    #Lo que queremos hacer dentro del ciclo, en este caso imprimir el numero
    print(numero)
    #numero o contador para el numero de veces que deseamos recorrer el ciclos
    numero += 1

#Aqui utilizamos un booleano para mantener el ciclo activo hasta que cumpla alguna condicion    
while booleano:
    #Lo que queremos hacer dentro del ciclo, en este caso imprimir el numero
    print(numero)
    #numero o contador para el numero de veces que deseamos recorrer el ciclos
    numero += 1
    
    #Usamos un if para revisar alguna condicion y apagar ciclo
    if numero > 10:
        booleano = False
        #break, el break tambien funciona, y detiene completamente el proceso
    
    #print("Aqui termina el ciclo")
    #el print de arriba solo funciona si se utiliza alguna condicional, si se usa el break no imprime esa linea ya que 
    #el break detiene completamente el funcionamiento