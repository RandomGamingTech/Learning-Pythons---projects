#El loop for nos permite iterar una cantidad específica de vueltas. 
#El número de vueltas que dará, está definido por los elementos que contenga la string
#La lista, o el diccionario.
#Por ejemplo, si una lista contiene 5 nombres, el loop for, dará 5 vueltas (se repetirá 5 veces).
#Otra propiedad del loop for, es que cada vuelta que da, es en relación VALOR del elemento, lo que quiere decir
#Que si tenemos una lista con [Ana, Juan, Carlos] la primera vuelta, tiene el valor de Ana, la segunda vuelta, tiene el valor
#De Juan, la tercera vuelta tiene el valor de Carlos.
#PODEMOS APROVECHAR ESTA PROPIEDAD, para interactuar con los valores de los elementos. Por ejemplo, si CONCATENÁRAMOS una lista con 
#Las vueltas del loop, quedaría algo así:
#lista = [Ana, Juan, Carlos]
#for element in lista
#   print("Hola" + element)
#>>Hola Ana
#>>Hola Juan
#>>Hola Carlos
#-----------------------------------------------------------------------------------------------------------------------------------------------
#EJEMPLO 1
#Este ejemplo nos imprime CADA LETRA.
#Esto porque en cada loop (VUELTA), pasó por la letra y la IMPRIMIÓ.
#lista = ["a","b","c"]
#for letra in lista:
    #print(letra)
#>>a
#>>b
#>>c
#---------------------------------------------------------------------------------------------------------------
#También podemos CONCATENAR los elementos con las VUELTAS.
#NOTE El nombre del ELEMENTO (en este caso, letra) NO IMPORTA!!!, solamente escogemos un nombre para que sea LEGIBLE
#El código.
#Aquí concatenamos CADA LETRA (elemento) con la string Letra

#lista = ["a","b","c","d"]

#for letra in lista:
   #print("Letra: " + letra)

#>>Letra a
#>>Letra b
#>>Letra c
#>>Letra d   

#---------------------------------------------------------------------------------------------
#EJEMPLO 2 Loop for e indice
#También es posible, obtener OTROS VALORES que podemos obtener CADA VEZ que vamos iterando por un objeto.
#No solamente con su valor directo:
#Aquí le pedimos a Python que nos devuelva el índice de la que EN ESE MOMENTO sea la letra por la que estoy
#pasando.
#Si dejáramos solamente lista.index(letra) sin agregar nada, comenzaría desde el índice 0; PERO EN ESTE CASO, 
#le sumamos 1, para que nos cuente desde el 1. 
#OJO QUE NO VA A CONTAR DESDE LA B (ÍNDICE 1), sino que Python contará desde el 1 PERO
#Respetará el ORDEN DEL CONTENIDO, por ejemplo. 1 a, 2 b, 3 c, 4 d.
 

#lista = ["a","b","c","d"]

#for letra in lista:
    #numero_letra = lista.index(letra) + 1
    #print(f"Letra {numero_letra}: {letra}")
    
#>>Letra 1: a
#>>Letra 2: b
#>>Letra 3: c
#>>Letra 4: d 

#----------------------------------------------------------------------------------------------------------------------------------------
#EJEMPLO 3 Loop con método startswith.()
#Aquí pediremos en el loop por CADA NOMBRE, una VERIFICACIÓN (if, elif, else)
#En este caso usamos el método startswith.() que nos SIRVE para VERIFICAR si un ELEMENTO COMIENZA con 
#DETERMINADA LETRA.
#Por cada VUELTA que de el bucle, Python verificará si CADA palabra comienza con la letra (en este caso) l.
#ESTO NOS IMPRIMIRÁ CADA NOMBRE QUE TENGA LA LETRA l. Esto porque pasó por cada ELEMENTO y los que TUVIERON l AL COMIENZO,
#los imprimió.
#Y como agregamos un else, recogió los demás nombres que no comenzaron con L, y simplemente imprimió lo que le indicamos en el print anidado en
#else ("Nombre que no comienza con L")
#POR ESO ES MAGNÍFICO COMBINAR LOS LOOPS CON EL CONTROL DE FLUJO.
#lista = ["pablo", "laura", "fede", "luis", "julia"]   

#for nombre in lista:
    #if nombre.startswith("l"):
        #print(nombre)
    #else:
        #print("Nombre que no comienza con L")

#>>Nombre que no comienza con L
#>>laura
#>>Nombre que no comienza con L
#>>luis
#>>Nombre que no comienza con L

#--------------------------------------------------------------------------------------------------------------------------------------
#EJEMPLO 4
#Ahora veremos otro ejemplo distinto.
#Aquí es fácil de descifrar por qué sucedió esto. En primera, EL VALOR INICIAL DE 0 era 0. Luego, EN EL BUCLE, le pedimos a Python que 
#mi_valor SE ACTUALICE a la suma de cada numero en la variable numeros. Entonces lo que sucedió fue:
#mi_valor inicial, 0, se sumó en la PRIMERA VUELTA, con 1. Luego, en la SEGUNDA vuelta, se SUMÓ con 2, y 1 (que es el valor que adquirió en la
#PRIMERA VUELTA) + 2 da 3, luego 3 + 3 da 6, 6 + 4 da 10, y 10 más el valor del elemento de la ÚLTIMA vuelta (5) da !!!!!15!!!!!
#numeros = [1,2,3,4,5] 
#mi_valor = 0

#for numero in numeros: 
    #mi_valor = mi_valor + numero
    
#print(mi_valor)
#>>15           

#Si el atenterior ejemplo a print le hubiéramos agregado UNA TABULACIÓN, entonces lo habríamos hecho PARTE del LOOP, y nos HUBIERA IMPRESO CADA PASO.
#Esto nos daría como resultado, 1, 3, 6, 10 y 15, es decir la SUMA de mi_valor, cuando PASÓ POR CADA número en la lista numeros.
#numeros = [1,2,3,4,5] 
#mi_valor = 0

#for numero in numeros: 
    #mi_valor = mi_valor + numero
    
    #print(mi_valor)
    
#>>1
#>>3
#>>6
#>>10
#>>15
#--------------------------------------------------------------------------------------------------------------------------------------------------
#EJEMPLO 5
#Nota, cuando pasamos un loop sobre una string, nos imprimirá CADA LETRA, ESPACIO Y CARACTER, que contenga la string, POR CADA VUELTA QUE DE.
#Como lo anterior explicado, nos imprimió python LETRA POR LETRA (una por cada vuelta)
#por eso PARA IMPRIMIR PALABRAS POR PALABRAS, usamos LISTAS.

#palabra = "python"

#for letra in palabra:
    #print(letra)
    
#>>p
#>>y
#>>t
#>>h
#>>o
#>>n

#NOTA, NO SIEMPRE ES NECESARIO TENER LA VARIABLE APARTE PARA BUCLEARLA. PODEMOS AGREGAR LA STRING EN EL MISMO BUCLE.
#NOTE Esto funciona TAMBIÉN en LISTAS, TUPLES Y DICCIONARIOS. Es decir, CUALQUIER OBJETO que se pueda ITERAR.
#Esto nos lo demuestra el siguiente ejemplo:

#for letra in "python":
    #print(letra)
    
#>>p
#>>y
#>>t
#>>h
#>>o
#>>n

#También PODEMOS ITERAR en una LISTA, que CONTENGA LISTAS:
#Como CADA lista DENTRO de la LISTA MADRE, es UN OBJETO, separado por una COMA (,) el bucle, nos imprime POR CADA VUELTA, UN ELEMENTO, o sea:
#[1,2]
#[3,4]
#[5,6]
#for objeto in [[1,2],[3,4],[5,6]]:
    #print(objeto)
    
#>>[1,2]
#>>[3,4]
#>>[5,6]

#¿Qué pasa si hubieramos querido imprimir CADA UNO de los OBJETOS dentro de las listas hijas?
#Ahí deberíamos haber creado DOS VARIABLES DENTRO del BUCLE.
#Lo que hacemos aquí, es que estamos creando DOS objetos, POR LO QUE EL BUCLE, pasa en el PRIMERO PARA a Y SE CARGA EL PRIMER VALOR DE LA SUB-LISTA, y luego
#pasa en el PRIMERO TAMBIÉN para b y SE CARA EL SEGUNDO VALOR DE LA PRIMERA SUB-LISTA, y así sucesivamente.
#IMPORTANTE, agregar DOS PRINTS, UNO PARA CADA OBJETO CREADO en el LOOP.
#Esto NOS DA CADA NÚMERO INDIVIDUAL (PORQUE A, SE CARGA CON UN ELEMENTO DE LA LISTA HIJA, Y B CON EL OTRO)
#AQUÍ EL EJEMPLO:

#for a,b in [[1,2],[3,4],[5,6]]:
    #print(a)
    #print(b)
    
#>>1
#>>2
#>>3
#>>4
#>>5
#>>6    
              
#--------------------------------------------------------------------------------------------------------------------------------------------------
#EJEMPLO 6 ITERAR EN UN DICCIONARIO
#EL SIGUIENTE BUCLE, SOLAMENTE IMPRIME LAS CLAVES, ya que CADA PAR tiene UN ITEM, y cada VUELTA, IMPRIME EL PRIMER ITEM (la clave)
#dic = {"clave1":"a","clave2":"b","clave3":"c"}

#for item in dic: 
    #print(item)

#>>clave1
#>>clave2
#>>clave3

#¿Cómo lo deberíamos haber hecho si queríamos IMPRIMIR los VALORES del diccionario?
#Aquí usaríamos el método dic.values()
#DE ESA MANERA SÍ NOS IMPRIMIRÍA LOS VALORES.

#dic = {"clave1":"a","clave2":"b","clave3":"c"}

#for item in dic.values(): 
    #print(item)
    
#>>a
#>>b
#>>c

#Si hubiéramos querido imprimir AMBOS ELEMENTOS del diccionario (clave y valor), lo hubiéramos hecho
#creando DOS variables en el loop y agregarle el método .items() al dic PARA QUE LAS DOS VARIABLES, RECOJAN
#LOS DOS ELEMENTOS DE CADA PARTE DEL DICCIONARIO.

#dic = {"clave1":"a","clave2":"b","clave3":"c"}

#for a,b in dic.items(): 
    #print(a,b)
    
#>>clave1 a
#>>clave2 b 
#>>clave3 c

#lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
#suma_numeros = 0
#for numero in lista_numeros:
    #suma_numeros = suma_numeros + numero
    #print(suma_numeros)

#--------------------------------------------------------------------------------------------------------------------
#
#EJERCICIOS CHAT GPT 1

#numeros = [15, 8, 3, 12, 10, 5, 7]

# Variable para almacenar la suma acumulativa de los cuadrados de los números impares
#suma_cuadrados_impares = 0

# TODO: Utiliza un bucle y el operador += para sumar los cuadrados de los números impares
#for numero in numeros:
    #if numero % 2 == 1:
        #suma_cuadrados_impares += numero
        #print(suma_cuadrados_impares)
        

# Imprime el resultado final
#print(suma_cuadrados_impares)

#---------------------------------------------------------------------------------------------------------------------------
#EJERCICIOS CHAT GPT 2
# Lista de nombres
#nombres = ["Juan", "María", "Carlos", "Ana", "Luis"]
#longitudes_nombres = []

#for letras in nombres:
    #longitudes_nombres.append(len(letras))

#print(longitudes_nombres)

# TODO: Utiliza un bucle y la función len() para contar cuántas letras tiene cada nombre
# Almacena el resultado en una lista llamada 'longitudes_nombres'

# Imprime la lista final de longitudes

#------------------------------------------------------------------------------------------------------------------------------
#
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares += numero
    elif numero % 2 == 1:
        suma_impares += numero  

print(suma_pares)
print("\n")
print(suma_impares)


          



    
    

    
    
    
    


        

   
    
        