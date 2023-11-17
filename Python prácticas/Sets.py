#EJEMPLO 1 
#Si imprimimos el tipo de valor que tiene un set, nos arrojará efectivamente,
#que es un tipo set. <class 'set'>
#Cuando imprimimos un set, se un conjunto de elementos entre llaves curvas.
#Este es una demostración de cuando imprimimos un set: {1, 2, 3, 4, 5} 
#Los sets, esperan que solo pongamos UN SOLO ARGUMENTO, por esa razón debemos
#encerrar los elementos aparte de los PARÉNTESIS ya puestos, en OTRAS LLAVES, como
#otros paréntesis, o unos corchetes o llaves curvas. En este caso, entre CORCHETES.
#mi_set = set([1,2,3,4,5])
#print(type(mi_set))
#print(mi_set)
#------------------------------------------------------------------------------
#EJEMPLO 2 Maneras de construir sets
# Podemos construir nuestro set también de la siguiente manera
#Las siguientes son las DOS formas en las que podemos crear un set.
#mi_set = set([1,2,3,4,5])
#print(type(mi_set))
#print(mi_set)

#otro_set = {1,2,3}
#print(type(otro_set))
#print(otro_set)
#-----------------------------------------------------------------------------------
#EJEMPLO 3 Los sets NO tiene ORDEN INTERNO
#Si quieremos buscar lo que hay en el índice 0, NOS ARROJARÁ ERROR.
#Lo que nos arroja el imprimir el index de un set es lo siguiente:
#TypeError: 'set' object is not subscriptable
#mi_set = set([1,2,3,4,5])
#print(type(mi_set))
#print(mi_set)

#print(mi_set[0])

#>>>TypeError: 'set' object is not subscriptable
#---------------------------------------------------------------------------------------
#EJEMPLO 4 NO podemos MODIFICAR los elementos de un set
#En este ejemplo, si invocamos a mi_set y queremos que su índice 0 se modifique a 5, nos 
#arrojará un error del siguiente tipo: TypeError: 'set' object does not support item assignment
#Esto nos da resultado: 
#mi_set = set([1,2,3,4,5])
#print(type(mi_set))
#print(mi_set)

#mi_set[0] = 5
#>>>TypeError: 'set' object does not support item assignment
#---------------------------------------------------------------------------------------
#EJEMPLO 5 LOS sets tienen elementos ÚNICOS, por lo que no podemos hacer repeticiones.
#Si repetimos un ELEMENTO que ya antes había tenido un set, Python los DESCARTARÁ
#El resultado de imprimir este set es: {1, 2, 3, 4, 5}
#Esto debido a que DESCARTÓ los elementos repetidos. 
#mi_set = set([1,2,3,4,5,1,1,1,2,2,2])
#print(type(mi_set))
#print(mi_set)
#>>>{1, 2, 3, 4, 5}
#----------------------------------------------------------------------------------------
#EJEMPLO 6 NO podemos almacenar LISTAS NI DICCIONARIOS en SETS
#Como un set no puede contener ELEMENTOS repetidos, esto quiere decir que TAMPOCO podemos 
#Tener como elementos LISTAS NI DICCIONARIOS.
#Ejecutar un set que tiene como lista uno de sus elementos, nos arrojará el siguiente error
#Resultado: TypeError: unhashable type: 'list'
#Esto también aplica para los DICCIONARIOS.
#mi_set = set([1,2,3,4,5,[2,1]])
#print(type(mi_set))
#print(mi_set)
#---------------------------------------------------------------------------------------
#EJEMPLO 7 Los sets SI admitirán TUPLES
#En el siguiente ejemplo, incluímos dentro del set un tuple que CONTIENE LOS MISMOS valores
#que YA ANTES tenía establecidos el set. ¿Cómo es esto posible?
#Esto es porque los tuples son INMUTABLES y esto mismo es lo que REQUIERE el SET, que sus elementos
#Sean INMUTABLES.
#mi_set = set([1,2,3,4,(1,2,3)])
#print(type(mi_set))
#print(mi_set)
#>>>{1, 2, 3, 4, (1, 2, 3)}
#---------------------------------------------------------------------------------------
#Ejemplo 8 PODEMOS USAR LA FUNCIÓN len
#Podemos usar la función len en un set para concer EL LARGO del mismo.
#El siguiente ejemplo nos imprimirá que el set tiene un LARGO de 5 elementos.
#Resultado: 5
#mi_set = set([1,2,3,4,5])


#print(len(mi_set))
#>>>5
#-------------------------------------------------------------------------------------
#EJEMPLO 9 Podemos hacer CONSULTAS con in 
#Podemos hacer consultas como en los strings. Por ejemplo, pedirle a python que nos diga
#Si DETERMINADO ELEMENTO se ENCUENTRA DENTRO de nuestro de nuestro SET.
#NOTE recordar que las consultas las hacemos con in
#Esto nos arroja un valor BOLEANO (True o False)
#En este caso, como el valor 2 SÍ está DENTRO de nuestro set, Python nos arroja True.
#Esto nos da como resultado: True
#NOTE 2, ESTO LO PODEMOS HACER CON LOS TUPLES, LAS LISTAS Y LOS DICCIONARIOS(en los
# diccionarios solo podemos consultar claves).
#mi_set = set([1,2,3,4,5])


#print(2 in mi_set)
#>>>True
#---------------------------------------------------------------------------------------
#EJEMPLO 10 UNION de SETS con .union()
#Ponemos AL PRINCIPIO la variable que contenga un SET, luego 
#DENTRO de los paréntesis de .union() la variable con la que lo queramos unir (que contenga
#otro set).
#como en este caso, UNIMOS en la variable s3 a s1 y s2 mediante .union, imprimir s3 nos da
#el siguiente resultado: {1, 2, 3, 4, 5}
#NOTE FÍJATE en CÓMO en la unión, python IGNORÓ los elementos que se REPETÍAN, en este caso,
#el 3 y solo lo imprimió UNA SOLA VEZ.
#s1 = {1,2,3}
#s2 = {3,4,5}
#s3 = s1.union(s2)
#print(s3)
#>>>{1, 2, 3, 4, 5}
#----------------------------------------------------------------------------
#EJEMPLO 11 AGREGAR ELEMENTOS CON ADD
#Podemos agregar elementos con .add()
#En este caso agregamos un 4 por medio de .add() method.
#el resultado es: {1, 2, 3, 4}
#NOTE si tratamos de agregar un elemento que YA ESTÁ, Python lo ignorará.

#s1 = {1,2,3}

#s1.add(4)

#print(s1)
#>>>{1, 2, 3, 4}
#----------------------------------------------------------------------------
#EJEMPLO 12 podemos ELIMINAR elementos con remove.()
#Para eliminar un elemento de nuestro tuple, lo INVOCAMOS en otra línea y aplicamos
#el método remove, luego entre sus paréntesis escribimos el elemento que queremos 
#eliminar
#El resultado de esto nos da: {1, 2}
#Si eliminamos un elemento que el set NO TIENE nos dará un error llamado: KeyError.

#s1 = {1,2,3}

#s1.remove(3)

#print(s1)
#>>>{1, 2}
#-----------------------------------------------------------------------------------
#EJEMPLO 13 método DISCARD con este método podemos DESCARTAR.
#Funciona exáctamente igual que remove, con la ÚNICA DIFERENCIA que si le pedimos que
#DESCARTE un elemento que NO TENEMOS dentro del set, NO NOS DARÁ ERROR
#Simplemente seguirá adelante como si no hubiera algún problema
#Ya que discard NO ES lo MISMO que remove.

#s1 = {1,2,3}

#s1.discard(6)

#print(s1)
#-------------------------------------------------------------------------------------
#EJEMPLO 14 MÉTODO .pop
#Este método nos sirve para saltar/eliminar un elemento.
#si escribimos el método .pop() y dejamos sus paréntesis VACÍOS nos eliminará UNO de sus
#ELEMENTOS, pero aquí como NO TENEMOS un órden (index) nos eliminará, un elemento ALEATORIO
#Este elemento nos puede servir para realizar una especie de sorteo porque podemos CONTENER
#al elemento eliminado DENTRO de una VARIABLE.
#
#s1 = {1,2,3}

#s1.pop()

#print(s1)
#--------------------------------------------------------------------------------------
#Continuamos con este mismo ejemplo, pero ahora para ponerlo un poco en práctica 
#crearemos un sorteo, almacenando el elemento aleatorio ELIMINADO por .pop() dentro de 
#una variable.
#En este caso, el número aleatorio que tocó fue el: 1 
#s1 = {1,2,3}

#sorteo = s1.pop()

#print(sorteo)
#>>>1
#--------------------------------------------------------------------------------------
#EJEMPLO 15 Método clear.() 
# Este método si dejamos sus paréntesis vacíos es VACIAR a nuestro set (lo limpia)
#Esto nos arrojará nuestro set SIN NINGÚN VALOR DENTRO.
#Resultado: set()
#s1 = {1,2,3}

#s1.clear()

#print(s1)
#>>>set()




    