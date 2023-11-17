#Ejemplo 1 diccionarios
#Al imprimer el type de un diccionario, nos da <class 'dict'>
#Si imprimimos la declaración diccionario, nos arroja su contenido,
#o sea, lo que está establecido entre llaves.
#El primer término, que es la clave, NO puede repetirse, el segundo término
#(que el valor) NO puede repetirse. 
#O sea, los valores pueden ser TODOS iguales y no pasaría nada. Pero las claves
#NO PUEDEN REPETIRSE.

#diccionario = {"c1":"valor1","c2":"valor2"}
#print(diccionario)

#--------------------------------------------------------------------
#EJEMPLO 2 consultar lo que hay DENTRO de las claves.
#para esto, almacenamos en una variable (en este caso la llamamos resultado)
#el index de diccionario establecido en la CLAVE c1.
#Esto nos arrojará el VALOR de la CLAVE c1.
#esto nos da como resultado: valor1 
 
#diccionario = {"c1":"valor1","c2":"valor2"}
#resultado = diccionario["c1"]
#print(resultado)
#-----------------------------------------------------------------
#Aquí tenemos un caso más realista de la vida real sobre la utilidad de la
#búsqueda de un valor en relación a la clave.
#Los diccionarios pueden contener DISTINTOS TIPOS DE DATOS en sus claves y valores.
#Esto quiere decir que incluso los diccionarios pueden CONTENER LISTAS, e 
#incluso también pueden contener diccionarios (así es, dentro de los diccionarios) 
#La variable consulta, nos ha arrojado fuentes como resultado, debido a que
#es lo que contiene la CLAVE del diccionario de cliente.
#cliente = {"nombre":"Juan", "apellido":"fuentes", "peso":88, "talla":1.76}
#consulta = cliente["apellido"]
#print(consulta)
#-------------------------------------------------------------------
#EJEMPLO 3 CONSULTAR índices de LISTAS dentro de una clave de un diccionario.
# 1.- Si imprimimos dic, nos arrojará todas las claves con sus valores.
# 2.- Si imprimimos dic con index de lo que haya en la CLAVE 2 ("c2") nos
#arrojará la lista: [10,20,30]
# 3.- Tenemos una FORMA para imprimir SOLAMENTE un DETERMINADO ÍNDICE de una 
# LISTA, almacenada en un DICCIONARIO. Y es de la siguiente manera:
# print(dic["c3"][1]) Esto nos arrojará 20, ya que como sabemos que la CLAVE 2
# CONTIENE una lista, entonces usamos un SEGUNDO CORCHETE, para consultar el 
# ÍNDICE de la lista (no del diccionario, sino DEL VALOR de la LISTA de la CLAVE).
#dic = {"c1":55,"c2":[10,20,30],"c3":{"s1":100,"s2":200}}
#print(dic["c2"][1])
#>>>20
#----------------------------------------------------------------
# EJEMPLO 4 Buscar DICCIONARIO dentro del DICCIONARIO
# Podemos almacenar diccionarios dentro de otras CLAVES de un Diccionario.
# al consultar la clave que contiene el diccionario, nos arroja, el diccionario
# almacenado en esa clave.
# Resultado {'s1': 100, 's2': 200}
#dic = {"c1":55,"c2":[10,20,30],"c3":{"s1":100,"s2":200}}
#print(dic["c3"])
#-----------------------------------------------------------------
# Buscar CLAVES de un diccionario, almacenados DENTRO de otro diccionario.
# Simplemente lo hacemos igual que en las listas, buscamos la clave donde se ubica
# EL DICCIONARIO luego agregamos OTROS corchetes, para buscar el índice de la clave 
# del diccionario GUARDADO dentro.
# Esto nos arroja 200, ya que es el valor que contiene la clave s2.
#dic = {"c1":55,"c2":[10,20,30],"c3":{"s1":100,"s2":200}}
#print(dic["c3"]["s2"])
#200
#---------------------------------------------------------------------
# EJERCICIO más elaborado de lo anteriormente explicado.
# En este ejercicio tuvimos que imprimir en pantalla la e pero en Mayúscula
# en una sola línea de código
# Lo hemos hecho con el método para string .upper() 
# Recordemos el método string .upper(), como el elemenento index 1 de la lista es
# una string, podemos aplicarle .upper()
#dic = {"c1":["a","b","c"], "c2":["d","e","f"]}
#print(dic["c2"][1].upper())
#-----------------------------------------------------------------
# EJEMPLO 5 agregar elementos a un diccionario.
#Para esto, INVOCAMOS dic y agregamos una nueva clave mediante corchetes
# luego declaramos que es "c", ahora SI IMPRIMIMOS NUEVAMENTE, ya nos 
#incluirá tanto la clave 3 como el valor "c".
# {1: 'a', 2: 'b'}
# {1: 'a', 2: 'b', 3: 'c'} 
# Se imprimen el viejo y el nuevo diccionario, ya que tenemos un antiguo
# print, y un NUEVO print de diccionario. 
# NOTA, esto NO QUIERE DECIR, que hayamos MODIFICADO la variable ORIGINAL, sino
# que fue insitum, lo que quiere decir, que SOLO lo hicimos EN EL SITIO. 
# No modificamos la variable ORIGINAL.

#dic = {1:"a",2:"b"} 
#print(dic)

#dic[3] = "c"

#print(dic)
#>>>{1: 'a', 2: 'b'}
#>>>{1: 'a', 2: 'b', 3: 'c'}
#------------------------------------------------------------------
#EJEMPLO 6 También podemos SOBREESCRIBIR un valor que YA existe.
#Por ejemplo, ahora queremos que la letra B, sea Mayúscula.
#Invocamos una CLAVE del diccionario y lo ASIGNAMOS a un nuevo valor, 
# (el cuál sería B) y ahora, Python nos da como resultado {1: 'a', 2: 'B'}
# Porque SOBREESCRIBIÓ un VALOR. 
#IMPORTANTE DISTINGUIR que no CREAMOS un nuevo valor, solo lo REESCRIBIMOS
# TAMBIÉN PODEMOS RESERVAR el VALOR sobreescrito.  

#dic = {1:"a",2:"b"} 

#dic[2] = "B"

#print(dic)
#-----------------------------------------------------------------
#EJEMPLO 7 Conocer TODAS LAS CLAVES que hay DENTRO de un diccionario.
# esto se logra con el MÉTODO .keys()
#Esto nos da LAS CLAVES.
#dict_keys([1, 2, 3])

#dic = {1:"a",2:"b"} 

#dic[3] = "c"

#print(dic.keys())
#-----------------------------------------------------------------
#EJEMPLO 8 si quisiéramos conocer TODOS los valores, lo haríamos con
#método .values()
#Esto nos arroja todos los VALORES del diccionario.
#dict_values(['a', 'b', 'c'])

#dic = {1:"a",2:"b"} 

#dic[3] = "c"

#print(dic.values())
#-----------------------------------------------------------------
#EJEMPLO 9 si queremos conocer TODO lo que hay dentro de un diccionario.
#Usamos el método .items
#Esto nos da como resultado TODOS los items
#dict_items([(1, 'a'), (2, 'b'), (3, 'c')])
#El hecho de que nos de 3 paréntesis nos indica que lo que hay dentro de un 
#Diccionario son Tuples. 

#dic = {1:"a",2:"b"} 

#dic[3] = "c"

#print(dic.items())

#>>>dict_items([(1, 'a'), (2, 'b'), (3, 'c')])

#EJERCICIO 2 DE DICCIONARIOS
#NOTA IMPORTANTE.
#Aquí, tenemos un caso donde nos piden crean una función print que devuelva el
#SEGUNDO ITEM de la lista llamada points2. 
#EN CUENTA, aquí en realidad tenemos solamente DOS CLAVES principales del 
#DICCIONARIO y 4 SUBCLAVES (v1, v2, points1, points 2)
#Por lo que en este ejercicio, debemos ESPECIFICAR la SEGUNDA CLAVE PRINCIPAL, la 
#CUARTA SUBCLAVE y el ÍNDICE 1 de sus VALORES.
#tenemos 2 DICCIONARIOS dentro
#Esto ya nos da el resultado deseado, que son, 300.
#mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
#print(mi_dict["puntos"]["points2"][1])
#-------------------------------------------------------------------
#EJERCICIO 3 DE DICCIONARIOS
#Luego tenemos este ejercicio donde nos piden ACTUALIZAR DOS datos de la información de
#este diccionario, y AGREGAR UNO nuevo. Aquí el ejercicio resuelto del
#ejercicio
#mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
#mi_dic["edad"] = 36
#mi_dic["ocupacion"] = "Editora"
#mi_dic["pais"] = "Colombia"
#print(mi_dic)
#>>>{'nombre': 'Karen', 'apellido': 'Jurgens', 'edad': 36, 'ocupacion': 'Editora', 'pais': 'Colombia'}
