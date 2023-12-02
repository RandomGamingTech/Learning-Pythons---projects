'''


--  Cómo vamos a realizar un código que requiere de muchas funciones, primero vamos a crear una especie de 
    guión de lo que vamos a hacer en este código:
    
    1.- Lista inicial
    2.- Función para mezclar palitos
    3.- Función pedirle al usuario un intento de que elija
    4.- Función de comprobar si el intento es acertado
'''

#lista inicial
palitos = ["-", "--", "---", "----"]

#función mezclar palitos
from random import *

def mezclar(lista):
    shuffle(lista)
    return lista


# print(mezclar(palitos)) #eliminamos esta linea porque solamente era para comprobar que sí mezclara la lista


#pedirle a un jugador que pruebe su suerte

def probar_suerte():
    intento = ""
    
    while intento not in ["1","2","3","4"]: #¿Por qué estamos escribiendo los números como strings y no como int? Eso es porque el usuario ingresará strings, aunque escriba integers. Este loop se activará instantáneamente porque la string está VACÍA.
        intento = input("Elige un numero del 1 al 4 ") #Este loop se repetirá tantas veces como sea necesario hasta que el usuario ingrese el número que corresponde
    return int(intento)

# intento1 = probar_suerte() #almacenamos nuestra definición dentro de una variable, posteriormente, la imprimimos.
# print(intento1) #luego eliminamos estas dos lineas de comprobación, una vez que vimos que funciona

#comprobar intento

def chequear_intento(lista,intento):
    if lista[intento - 1] == "-": #Aquí trabajamos con el ÍNDICE de la lista (recordar que inicia desde el 0) en el intento (el número que ingrese el usuario le restamos 1 para que concuerde con el ÍNDICE de la lista) x es igual al "-" el palito más corto, entonces: 
        print("A lavar los platos")
    else:
        print("Esta vez te has salvado")
        
    print(f"Te ha tocado {lista[intento-1]}")
    
    '''
    --  Lo anterior no imprimirá nada debido a que las funciones aún no están conectadas... 
    '''
    
palitos_mezclados = mezclar(palitos) #guardamos en esta variable la INVOCACIÓN de nuestra función mezclar y le ponemos como argumento la lista palitos

seleccion = probar_suerte() #Luego invocamos nuestra función probar_suerte() (la cual no requiere parametro) para que el usuario ingrese su intento

chequear_intento(palitos_mezclados,seleccion) #Al final invocamos nuestra funcion chequear_intento sin guardarla en ninguna variable, ya que esta NO DEVUELVE NADA (no tiene return, solo imprime)
                                                #Esta función recordemos que hicimos que nos pida tanto la lista (ya mezclada por la función 1) invocada en la variable palitos_mezclados como el intento del jugador (que se obtuvo en la función 2) invocada en la variable seleccion
                                                #NOTE ES BIEN IMPORTANTE que INVOQUEMOS A LAS DEFINICIONES EN ORDEN, de otra manera NO FUNCIONARÁ.
                                                
                                                