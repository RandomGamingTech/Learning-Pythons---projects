#EJEMPLO 1
#Creamos una lista de 3 elementos, e imprimimos el TYPE de datos
#para ver qué tipo de datos arroja, arrojó "list"
#mi_lista = ["a","b","c"]
#print(type(mi_lista))
#>>>list
#----------------------------------------------------------------
#EJEMPLO 2
#Podemos crear listas que tengan DIFERENTES tipos de datos.
#El type sigue siendo "list" aunque tengamos DIFERENTES tipos de
#datos (string, integer y float)  
#mi_lista = ["a","b","c"]
#otra_lista = ["hola", 55, 6.1]
#print(type(otra_lista))
#----------------------------------------------------------------
#EJEMPLO 3 len

#Podemos aplicar la función len a una lista para que nos diga
# el LARGO de la lista. Cada ELEMENTO de la lista lo considerará
# y lo contará.
#El resultado de len de la siguiente lista es 3
#mi_lista = ["a","b","c"]
#resultado = len(mi_lista)
#print(resultado)
#>>>3
#-----------------------------------------------------------------
#EJEMPLO 4 index

#También podemos EXTRAER el VALOR de uno de sus ELEMENTOS con 
#INDEX, o sea, podemos INDEXAR a las listas
#El resultado de indexar el elemento 0 de la siguiente lista nos da
#a
#Al igual que en las strings los ÍNDICES comienzan desde 0.
#mi_lista = ["a","b","c"]
#resultado = mi_lista[0]
#print(resultado)
#>>>a
#---------------------------------------------------------------------
#todo lo que hemos aprendido de index en strings, se puede aplicar en 
#Las listas, como vemos en el siguiente ejemplo.
#El resultado de buscar desde 0 hasta 1, nos da ["a"] (esta vez 
# entre comillas y corchetes debido a que buscamos más ELEMENTOS), porque el rango
#máximo, (que es 1) NO nos PERMITE mostrar la "b".
#mi_lista = ["a","b","c"]
#resultado = mi_lista[0:1]
#print(resultado)
#>>>["a"]
#----------------------------------------------------------------------
#También, igual que en strings, si nosotros ponemos el primer número de index
#y dejamos dos puntos VACÍOS luego del primero y no rellenamos nada, nos 
#MOSTRARÁ TODOS los elementos de la lista.
#Esto nos da ['a', 'b', 'c']
#mi_lista = ["a","b","c"]
#resultado = mi_lista[0:]
#print(resultado)
#>>>['a', 'b', 'c']
#--------------------------------------------------------------------------
#EJEMPLO 5 concatenar

#También podemos imprimir CONCATENACIONES de listas
#Aquí obtuvimos ['a', 'b', 'c', 'd', 'e', 'f'] básicamente al concatenar
#estas letras, lo que obtuvimos fue unirlas pero SIN LOS CORCHETES.
#Recordar que al concatenar DENTRO de print, las listas originales 
#SIGUEN EXISTIENDO, solamente nos ha IMPRESO una CONCATENACIÓN de ambas listas.
#mi_lista = ["a","b","c"]
#mi_lista2 = ["d", "e", "f"]
#print(mi_lista+mi_lista2)
#-----------------------------------------------------------------------------
#Si lo que queremos es que LAS DOS, existan en UNA SOLA lista, para poder usarla
#EN ADELANTE, lo que tenemos que hacer es crear una TERCERA LISTA que SUME 
#(o concatene) AMBAS LISTAS.
#Y ya si imprimimos mi_lista3 sería independiente.
#mi_lista = ["a","b","c"]
#mi_lista2 = ["d", "e", "f"]
#mi_lista3 = mi_lista + mi_lista2
#print(mi_lista3)
#---------------------------------------------------------------------------------
#EJEMPLO 7 concatenar en una variable.

#Hay cosas que una lista SÍ puede hacer sobre una string, que es CONCATENAR sus 
#elementos. 
#Lo que logramos en este ejemplo es que al MODIFICAR mi_lista3 mediante INDEX,
#Vemos que SÍ SE MODIFICAN al elemento que nosotros establecemos. Y ahora 
#mi_lista3 en VEZ de que su elemento 0 sea "a" ahora es "alfa"
#esto nos da como resultado: ['alfa', 'b', 'c', 'd', 'e', 'f']
#mi_lista = ["a","b","c"]
#mi_lista2 = ["d", "e", "f"]
#mi_lista3 = mi_lista + mi_lista2

#mi_lista3[0] = "alfa" 

#print(mi_lista3)
#------------------------------------------------------------------------------------
#EJEMPLO 8 añadir elementos con .append()

#También tenemos MÉTODOS para hacer muchas cosas con las listas.
#El método .apend() nos permite AGREGAR elementos a la lista.
#append en inglés significa ADJUNTAR
#En este ejemplo agregamos con append el elemento "g" y nos lo incluye al imprimirlo.
#el resultado de esto es: ['a', 'b', 'c', 'd', 'e', 'f', 'g']

#Nota, AGREGAR elementos con .append() NO ES una concatenación. Sino que MODIFICAMOS la
#lista y AÑADIMOS

#!!!!!!!!!!!NOTA SUPER IMPORTANTÍSIMA!!!!!!!!!!!!!!! NO PODEMOS AÑADIR ELEMENTOS CON
#.append() DENTRO DE PRINT. DEBEMOS PRIMERO ACTUALIZAR LA VARIABLE CON .APPEND Y LUEGO
#YA IMPRIMIRLO. NO ALMACENARLO EN VARIABLES, SOLO ACTUALIZARLO. COMO EN EL EJEMPLO.

#mi_lista = ["a","b","c"]
#mi_lista2 = ["d", "e", "f"]
#mi_lista3 = mi_lista + mi_lista2

#mi_lista3.append("g") 

#print(mi_lista3)
#>>>['a', 'b', 'c', 'd', 'e', 'f', 'g']
#-----------------------------------------------------------------------------------------
#EJEMPLO 9 ELIMINAR elementos de una lista método .pop()
#El método .pop() nos permite eliminar elementos de una lista.
#Pop en inglés significa SALTAR.
#Si dejamos .pop() con sus paréntisis VACÍOS lo que va a interpetar Python es que quieres
#ELIMINAR el ÚLTIMO de sus elementos.
#Este pop, nos elimina el elemento "f" debido a que dejamos los paréntesis VACÍOS.
#mi_lista = ["a","b","c"]
#mi_lista2 = ["d", "e", "f"]
#mi_lista3 = mi_lista + mi_lista2

#mi_lista3.pop() 

#print(mi_lista3)
#------------------------------------------------------------------------------------------
#Si especificamos a .pop() cuál es el ÍNDICE que queremos eliminar (o saltar), eliminará
#ESE elemento en ESPECÍFICO.
#El siguiente ejemplo nos da ['b', 'c', 'd', 'e', 'f'] debido a que .pop(0) eliminó el 
#elemento 0 de la lista.
#mi_lista = ["a","b","c"]
#mi_lista2 = ["d", "e", "f"]
#mi_lista3 = mi_lista + mi_lista2

#mi_lista3.pop(0) 

#print(mi_lista3) 
#>>>['b', 'c', 'd', 'e', 'f']
#-----------------------------------------------------------------------------------------
#También hay una forma de ALMACENAR ese elemento que eliminamos para RESERVARLO
# en una variable y no es mas que otra cosa que CREAR una NUEVA VARIABLE que almacene 
# El caracter ELIMINADO de la lista.
#Esto imprime:
#['b', 'c', 'd', 'e', 'f']
#a 

#mi_lista = ["a","b","c"]
#mi_lista2 = ["d", "e", "f"]
#mi_lista3 = mi_lista + mi_lista2

#eliminado = mi_lista3.pop(0) 

#print(mi_lista3)
#print(eliminado)
#>>>['b', 'c', 'd', 'e', 'f']
#>>>a 
#--------------------------------------------------------------------------------------------
#EJEMPLO 10 ORDENAR las listas. .sort()
#sort en inglés significa ORDENAR/CLASIFICAR (también tipo)
#en este caso, .sort() nos ordenó estas letras en ÓRDEN ALFABÉTICO. Lo mismo hubiera pasado
#con números, nombres de personas, etc.
#NOTE LAS LISTAS NO DEVUELVEN RESULTADO, SOLO ACTÚAN IN PLACE. Por ejemplo, siquieremos imprimir
#print(lista.sort())
#Nos devolverá none, ya que solamente podemos modificarla IN PLACE INVOCANDO A LA VARIABLE.
#EN RESUMEN, un método in-place NO CREA otra NUEVA LISTA.
#EJEMPLO
# Ejemplo de método in-place
#mi_lista = [1, 2, 3]
#mi_lista.append(4)  # El método append() modifica la lista original en lugar de crear una nueva lista

# Ejemplo de método no in-place
#mi_lista = [1, 2, 3]
#nueva_lista = mi_lista + [4]  # Aquí se crea una nueva lista en lugar de modificar la original

#lista = ["g", "o", "b", "m", "c"] 
#lista.sort()
#print(lista)
#-------------------------------------------------------------------------------------------
#Tener en cuenta que sort es un método que trabaja EN EL LUGAR, lo que quiere decir que sí 
#reordena la lista pero no es un MÉTODO que DEVUELVA ALGO.
#Esto significa que si queremos guardar el .sort() de una lista en UNA NUEVA VARIABLE, nos arrojará
#None
#Incluso si imprimimos el type de nueva_lista, nos saldrá NoneType, el cuál es el TIPO de dato
#de un NO OBJETO. O sea, un OBJETO que NO tiene Valor. 
#En resumen, .sort() es un MÉTODO de ACCIÓN, que no DEVUELVE nada, por lo tanto, a esa NO 
#DEVOLUCIÓN no la podemos asignar a una variable.
#lista = ["g", "o", "b", "m", "c"] 
#nueva_lista = lista.sort()
#print(nueva_lista)
#>>>None
#--------------------------------------------------------------------------------------------
#EJEMPLO 11 Ordenar INVERSAMENTE reverse.()
#Nos permite ordenar los elementos de nuestra lista de forma INVERSA
#Al igual que .sort() reverse NO DEVUELVE NADA, solo transforma la lista 
#EN EL LUGAR.
#En este ejemplo, primero tenemos que la lista la ordena .sort() y queda en ÓRDEN ALFABÉTICO
#Luego, tenemos que .reverse() la reordena (porque se actualiza la variable) y la ordena de la 
#Z a la A.
#lista = ["g", "o", "b", "m", "c"]
#lista.sort() 
#lista.reverse()
#print(lista)
#redes = ["YouTube", "Facebook", "Twitter", "Whatsapp"]
#redes.sort()
#print(redes)


