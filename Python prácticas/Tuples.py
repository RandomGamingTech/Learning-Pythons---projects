#EJEMPLO 1
#Si imprimimos el TIPO de dato, nos da <class 'tuple'>.
#Los tuples también FUNCIONAN IGUAL si NO les ponemos paréntesis.
#Lo más común es construirlos con paréntesis, pero es preferencia personal.
#mi_tuple = (1,2,3,4)
#print(type(mi_tuple))
#----------------------------------------------------------------------------
#Ejemplo 2 INDEXAR Y FRACCIONAR TUPLES
#valores, mezclados en un solo tuple. 
#Podríamos tener incluso otro tuple, dentro de un tuple, un diccionario, una lista...
#PODEMOS INDEXAR y FRACCIONAR tuples.
#En este ejemplo, como busca el índice 0, nos arroja 1.

#mi_tuple = (1,2,3,4)

#print(mi_tuple[0])
#>>>1
#-----------------------------------------------------------------------------------
#También podemos investigar con NÚMEROS NEGATIVOS, que al igual que las strings
#Esto hace que se cuente, de derecha a izquierda
#La posición -2 es la del factor 3.
#mi_tuple = (1,2,3,4)

#print(mi_tuple[-2])
#>>>3
#----------------------------------------------------------------------------------
#EJEMPLO 3 Los tuples son INMUTABLES
#Si declaramos que index 0 de la variable ahora es 5, esto nos arrojará el siguiente error.
# TypeError: 'tuple' object does not support item assignment
#mi_tuple = (1,2,3,4)

#mi_tuple[0] = 5

#print(mi_tuple)
#>>>TypeError: 'tuple' object does not support item assignment
#--------------------------------------------------------------------------------------
#EJEMPLO 4 PODEMOS ANIDAR
#Podemos anidar. Por ejemplo, podemos tener dentro de nuestro tuple UNO o MÁS elementos 
#que sean tuples
#Si consultamos a Pyrhon qué elemento tenemos en la posición 2, nos arrojará el tuple que 
#está en la posición 2
#(10, 20)
#mi_tuple = (1,2,(10,20),4)


#print(mi_tuple[2]) 
#---------------------------------------------------------------------------------------
#Para consultar el primero de los elementos que HAY DENTRO de ese tuple, ponemos otros
#corchetes para indicarle a python la posición del elemento que está DENTRO del tuple.
#Consultar de esta manera, nos da el PRIMER elemento DENTRO DEL TUPLE que se encuentra en
# LA POSICIÓN 2,
#Nos da como resultado: 20 
#mi_tuple = (1,2,(10,20),4)


#print(mi_tuple[2][0])
#>>>20
#---------------------------------------------------------------------------------------
#EJEMPLO 5 HACER CASTING (fundir, convertir)
#Lo podemos fundir con otros elementos. Esto quiere decir que lo podemos CONVERTIR a otro
# tipo de elemento.
#Si imprimimos el type del siguiente ejemplo nos arrojará: <class 'list'>
#mi_tuple = (1,2,(10,20),4)

#mi_tuple = list(mi_tuple)


#print(type(mi_tuple))
#----------------------------------------------------------------------------------------
#Si ahora lo sobreescribimos, y lo convertimos en un tuple luego de haberlo convertido en
#lista, nos arrojará que ahora es tuple.
#Resultado: <class 'tuple'>
#mi_tuple = (1,2,(10,20),4)

#mi_tuple = list(mi_tuple)

#mi_tuple = tuple(mi_tuple)

#print(type(mi_tuple))
#>>><class 'tuple'>
#--------------------------------------------------------------------------------------
# EJEMPLO 6 Asignar el CONTENIDO de un tuple a DIFERENTES VARIABLES.
#Si asignamos que x,y,z tengan el valor de lo que EXISTA en T (tuple), x,y,z tendrán
#los valores 1,2,3 de la variable t.
#Esto lo puede hacer porque al tener la MISMA cantidad de valores que de VARIABLES, 
#se asignaron una a una con este proceso.
# NOTE ESTO SE PUEDE HACER TAMBIÉN CON LAS LISTAS Y LOS DICCIONARIOS, PERO SIEMPRE QUE HAYA
#LA MISMA CANTIDAD DE VALORES Y VARIABLES!!!, SI NO DARÁ ERROR, PORQUE NO HABRÁN SUFICIENTES
#VALORES PARA DESEMPACAR.
#Esto nos da como resultado: 1 2 3
#t = (1,2,3)

#x,y,z = t

#print(x,y,z)
#---------------------------------------------------------------------------------------
#EJEMPLO 7 Método len() vs MÉTODO .COUNT()
#Si consultamos con len el largo de la variable t, nos dará 4
#t = (1,2,3,1)

#print(len(t))
#-------------------------------------------------------------------------------------
#Ahora consultamos su largo con uno de los DOS métodos que tienen los tuples 
#.count() e .index()
#.count() nos PIDE un PARÁMETRO dentro de sus PARÉNTESIS, que es QUÉ ES lo que queremos
#contar para saber CUÁNTAS VECES APARECE.
#Esto nos arrojará que el ELEMENTO 1 del tuple de la variable t, se REPITE 2 veces.
#EN RESUMEN, tuple nos permite CONTAR la CANTIDAD de APARICIONES hay de un VALOR DENTRO del
#tuple.
#Nos da como resultado: 2
#t = (1,2,3,1)


#print(t.count(1))
#>>>2
#--------------------------------------------------------------------------------------
#EJEMPLO 8 método .index()
#Dentro de los paréntesis .index() podemos poner cuál es el VALOR que queremos CONSULTAR
#su NÚMERO DE ÍNDICE.
#En este caso le preguntamos a Python en qué ÍNDICE se ENCUENTRA el valor 2.
#El resultado es que está en el índice 1.
#t = (1,2,3,1)


#print(t.index(2))
#------------------------------------------------------------------------------------
#
#t = (1,2,3,1)


#print(t.index(2))

#Los tuples no son un tipo de VALOR que vayamos a usar con MUCHA frecuencia al 
# COMIENZO de nuestra carrera.


