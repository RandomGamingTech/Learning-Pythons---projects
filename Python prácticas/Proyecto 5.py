'''
--  Programar el ahorcado
    1.- Tendremos que importar choice para que nos devuelva una palabra al azar dentro de una lista de palabras (que tenemos que crear).
    2.- Crear funciones paara:
        - pedir letra
        - validar letra
        - Chequear letra
        - verificar letra
    Nota, primero escribir las funciones y luego escribir el código que las implementa.
    Consejos

'''
def escoger_palabra():
    from random import choice
    palabras = ["Avion", "Cocinero", "Madera", "Paracetamol", "Auto", "Mansion", "Paloma", "Cascarrabias", "Felicidad", "Python"]
    elegida = choice(palabras)
    
    print("He pensado en una palabra, cada guión que hay en la siguiente lista\nrepresenta una letra de la palabra, ¡trata de adivinar la palabra letra por letra!")
    return elegida

def mostrar_guiones(elegida):
    guiones = []
    
    for letra in elegida:
        guiones.append("-")
    print(guiones)
    return guiones
    
    
def pedir_letra():
    intento = "" #Si queremos hacer que el usuario ingrese un carácter específico de entre una lista de carácteres permitidos, tenemos que usar una string vacía (debido a que input genera strings)
    letras_permitidas = [chr(A) for A in range(ord("a"), ord("z") + 1)] + [chr(A) for A in range(ord("A"), ord("Z") + 1)] #compresión de lista que nos permite obtener una lista de carácteres de la a-z y A-Z
    
    while intento not in letras_permitidas:
        intento = input("Ingresa UNA SOLA letra que creas que pertenece a la palabra (no números\nni carácteres especiales): ") #actualizamos intento para que ingrese un carácter válido.
        if len(intento) > 1:
            intento = input("¡Ingresa solamente una letra! ")
    
    else: #Si intento sí está en letras permitidas, que nos devuelva el intento.
        intento in letras_permitidas
        return intento
        

def validar_letra(intento,elegida,guiones):
    vidas = 8
    intentos_fallidos = []
    
    if intento in elegida:
        indice_intento = elegida.index(intento) #declaramos una variable que ALMACENA el ÍNDICE que tiene intento dentro de la variable elegidas (por choice)
        guiones[indice_intento] = intento #El número de índice que haya en la lista de guiones será sustituído por el número de índice que haya en la variable elegidas.
        print(f"A continuación, te mostraré en qué lugar de la palabra está tu letra: {guiones}")
    else:
        while intento not in elegida:
            vidas -= 1
            intentos_fallidos.append(intento)
            
            intento = input(f"Tu palabra no está en la palabra que pensé, te quedan {vidas} vidas. Intenta otra vez {guiones}: ")
            if vidas != 0:
                continue
            else:
                print("Se te han acabado las vidas. Intenta nuevamente en otra ocasión.")
                break
        while guiones != elegida:
            intento = input(f"¡Muy bien!, haz adivinado una letra, sigue con las demás: {guiones} ")
        if guiones == elegida:
            print(f"¡Haz ganado, felicitaciones!.\nEstos son los intentos que hiciste {intentos_fallidos}")
    
        
palabra = escoger_palabra()

guiones = mostrar_guiones(palabra)

pedir = pedir_letra()

validar = validar_letra(pedir,palabra,guiones)


# Bienvenida = print("Hola, bienvenido al juego del ahorcado. Tienes 8 vidas para tratar de adivinar la palabra que estoy pensando...")

# reto = input("¿Aceptas el reto? (escribe 'y' para sí y 'n' para no:) ")

# while reto != "y" and reto != "n":
#     print("Caracter equivocado, por favor ingresa 'y' para sí y 'n' para no ")
#     reto = input("Ingresa un 'y' para sí y 'n' para no; ")
    
# while reto == "y" or reto == "n":
#     if reto == "n":
#         print("\n¡Hasta la próxima!")
#         break
#     else:
#         continue

    
        