#métodos y propiedades de string
#indexar estructuras de datos
#todos los tipos de datos
#Programar analizador de texto
#1.- Le pedimos al usuario que ingrese un texto. Puede ser un párrafo, un artículo entero, 
#una frase o un poema (lo que el quiera)
#2.- El programa le pide que ingrese 3 letras a su elección.
#3.- El código procesará la información para hacer CINCO tipos de análisis y lo que hará
#es devolverle al usuario la siguiente información:
    #1.-Cuántas veces aparece cada letra. O sea, almacenar esas letras en una lista y luego
    #usar un método de string que nos permita CONTAR cuántas veces aparece un SUB-STRING.
    #Para que no afecte el resultado si están en mayúsculas o minúsculas es PASAR TANTO el 
    #TEXTO ORIGINAL como LAS LETRAS A BUSCAR en minúsculas. 
    #2.- Le diremos al usuario CUÁNTAS PALABRAS HAY a lo largo de todo el texto. Por lo que
    #recordemos que hay un método de string que permite transformarlo en UNA LISTA y UNA FUNCIÓN
    #que PERMITE averigual el LARGO de una lista.
    #3.- Informar cuál es la primera letra del texto y cuál es la ÚLTIMA. (indexación)
    #4.- Palabras en orden inverso. El sistema nos mostrará cómo quedaría el texto si INVIRTIÉRAMOS
    #el ORDEN de las PALABRAS (método que permita invertir UNA LISTA y otro que permita UNIR esos
    # elementos con ESPACIOS INTERMEDIOS). 
    #5.- Nos dirá si la palabra python, se encuentra dentro del texto. Podemos usar, booleanos para
    # realizar nuestra averiguación y un DICCIONARIO para encontrar la MANERA de expresarle al usuario
    #su respuesta.

print("Bienvenido al Analizador de Textos 1.0")
Texto = input("Ingresa tu texto: ")
Letras = input("Ingresa 3 letras de tú elección SIN ESPACIOS: ")
Texto = Texto.lower()
Letras = Letras.lower()
Letras = list(Letras)
Letra1 = Letras[0]
Letra2 = Letras[1]
Letra3 = Letras[2]
Contador1 = Texto.count(Letra1)
Contador2 = Texto.count(Letra2)
Contador3 = Texto.count(Letra3)
print(f"Tu letra \"{Letra1}\" aparece {Contador1} veces, la letra \"{Letra2}\" aparece {Contador2} veces y tu letra \"{Letra3}\" aparece {Contador3} veces en tu texto")

print("\n")

Texto2 = Texto.split()
print(f"En tu texto hay {len(Texto2)} palabras")

print("\n")

print(f"La primera letra de tu texto es \"{Texto[0]}\" y la última es \"{Texto[-1]}\"")

print("\n")

Texto2.reverse()

Texto3 = " ".join(Texto2)
print(f"Tu texto invertido sería {Texto3}")

print("\n") 

consulta = "python" in (Texto)
diccionario = {"es":consulta}

print(f"¿Tu texto contiene la palabra \"Python\"? --{diccionario["es"]}--")

#if consulta is True:
    #print("Tu texto sí contiene la palabra \"Python\" ")
#else:
    #print("Tu texto no contiene la palabra \"Python\"")
    
print("\n")    













 