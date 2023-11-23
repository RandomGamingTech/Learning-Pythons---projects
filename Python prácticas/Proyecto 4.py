'''
Proyecto adivina el número.

Usaremos:
- Operadores de comparación
- Operadores lógicos
- Control de flujo
- loops
- random, zip, range etc.

Características:

1.- El programa le preguntará al usuario su nombre y luego le va a decir algo como
    "Juan, he pensado un número entre el 1 y el 100 y tienes solo 8 intentos para intentar
    adivinar, ¿cuál crees que es el número?"
2.- En cada intento el jugador dirá un número y el programa puede responder CUATRO cosas distintas.

    2-1.- Si el número que dijo el usuario es MENOR a 1, o SUPERIOR a 100, le va a decir algo como 
            "error, tu número es menor a 1 o mayor a 100"
    2-2.- Si el número que ha elegido el usuario es MENOR o MAYOR al que ha pensado el programa, le va a decir que
            su respuesta no es correcta y que ha elegido un número menor al numero secreto.
    2-3.- Si el usuario acertó el número secreto, le informará al usuario que ha ganado y CUÁNTOS INTENTOS LE HA TOMADO.



'''

nombre = input("Hola, ¡bienvenido al juego de 'Adivina el número'! \n\n¿Cuál es tu nombre?: ")
print(f"\n{nombre}, he pensado un número ENTERO de entre 1 al 100, tienes OCHO intentos para tratar de adivinar...")
from random import *
numero = randint(1,100)
veces = 0

acepta = input("¿Aceptas el reto? (y/n): ")

while str(acepta):
    if acepta != "y" and acepta != "n":
        print("Debes ingresar 'y' para si y 'n' para no, favor de reintentar...")
        acepta = input("Escribe 'y' o 'n': ")
    elif acepta == "y":
        supuesto_numero = int(input("\nIngresa el número ENTERO que crees que estoy pensando: "))
        while supuesto_numero != numero and veces < 8:
            veces += 1
            if veces == 8:
                print("Haz agotado tu número de intentos, adiós.")
                break
        if supuesto_numero < 1 or supuesto_numero > 100:
                print("Tu número no está dentro de los parámetros (debes ingresar un número de entre 1 al 100)")
        elif supuesto_numero < numero:
                print("Tú número es menor que el que pensé :(")
        elif supuesto_numero > numero:
                print("Tu número es mayor al que pensé :(")
        if supuesto_numero == numero:
            print("Haz ganado, tu número es el que pensé! :D ")
            break
    elif acepta == "n":
        print("\nVuelve cuando tengas las agallas >:( ")
        break
        
                #print(f"Tu número ES EL QUE PENSÉ :D \n te ha tomado ")
                #i
    
        
        
'''        
from random import *
numero = randint(1,100)
numero_participante = input("Escribe el número que creas que estoy pensando: ")
'''

'''
acepta = input("\n¿Aceptas el reto? (y/n): ")

while acepta != "y" and acepta != "n":
    print("Debes escribir 'y' o 'n' ")
    acepta = input("Escribe un valor correcto: ")
    
while acepta == "n":
    print("Adiós")
    break
    
from random import *
numero = randint(1,100)

supuesto_numero = int(input("Escribe tu número: "))

while supuesto_numero == int:
    if supuesto_numero < 1 or supuesto_numero > 100:
        print("Error, tu número  NO ESTÁ dentro de los parámetros")
    elif supuesto_numero > numero:
        print("Tu número es mayor al número que pensé :( ")
    elif supuesto_numero < numero:
        print("Tu número es menor al que pensé :(") 
    elif supuesto_numero == numero:
        print("ACERTASTE!! Tú número es el que pensé")
'''


    



    
    
    