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

nombre = input("Hola :D ¿cuál es tu nombre: ")
instrucciones = print(f"\nHola {nombre}, ¡bienvenido al juego de 'adivina el número'!, las reglas son las siguientes: Debes de escribir un NÚMERO entero de entre el 1 al 100.\nNO debes escribirlo con letra, ni tampoco con punto decimal (de lo contrario el programa marcará error y tendrás que reintentarlo de nuevo en otra ocasión).")
acepta = input(f"\n¿Quieres participar? (responde 'y' para sí y 'n' para no): ")
from random import *
numero = randint(1,100)
veces = 0

while str(acepta):
    if acepta != "y" and acepta != "n":
        print("Debes ingresar 'y' para sí y 'n' para no")
        acepta = input("Ingresa 'y' para sí y 'n' para no: ") #Para que el bucle no se EJECUTE INFINITAMENTE, debemos tener una variable YA ESTABLECIDA, y si NO se cumple, ACTUALIZARLA en el MISMO BUCLE (ES IMPORTANTE TENER UNA VARIABLE anteriormente ya establecida.)
    elif acepta == "y":
        supuesto_numero = int(input("Ingresa el número que crees que estoy pensando (un número ENTERO del 1 al 100): "))
        if supuesto_numero < 1 or supuesto_numero > 100: #IMPORTANTE. Para respetar el flujo del programa, PRIMERO, ponemos esta condición, para que supuesto número NO sea ni menor a 1 ni mayor a 100. 
            print("Error, debes ingresar un número del 1 al 100 (tu número ingresado fue mayor a 100 o menor a 1)")
        elif supuesto_numero != numero:
            veces = veces + 1
            if veces == 8:
                print(f"\n{nombre}, haz excedido el número de intentos permitidos (8), te esteremos esperando en otra ocasión :) ")
                break
            elif supuesto_numero > numero: #Nota importantísima: Como CONDICIÓN, de que supuesto número SEA IGUAL a número NO se cumple, entonces que supuesto numero sea MAYOR o MENOR que número, ENTRA DENTRO de la IDENTACIÓN del condicional != numero
                print("\nTu número es MAYOR al que pensé :( ")
            elif supuesto_numero < numero:
                print("\nTu número es MENOR al que pensé :( ") 
        else: #Aquí usamos un else, debido a que la condición del if ""
            print(f"\nFelicidades {nombre}, ¡haz ganado :D! Te ha tomado {veces} intentos adivinar el número")
            break
    else: #Aquí usamos else, ya que tenemos DOS condiciones en la primera línea de if, donde si acepta NO es y y acepta NO es n... Como tenemos un condicional donde si acepta LLEGA a ser y, entonces hacemos algo... pero como NO hay una condición específica para n, entonces lo recoge ELSE.
        print("Vuelve cuando tengas las agallas >:( ")
        break
    
