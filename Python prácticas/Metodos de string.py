#EJEMPLO 1 MÉTODO UPPER
#Los métodos se escriben con un par de paréntesis subsecuentes para decirle
#al sistema que estamos trabajando con un método. Muchas veces estos paréntesis
#no van a contener nada, porque el método puede que no necesite más información
#Aquí, upper obviamente nos transforma el texto a Mayúsculas.
#El resultado de este ejercicio es: ESTE ES EL TEXTO DE FEDERICO
#texto = "Este es el texto de Federico"

#resultado = texto.upper()

#print(resultado)
#---------------------------------------------------------------------------
#Ejemplo 4
#Si queremos por ejemplo, convertir a mayúscula una DETERMINADA letra, podemos
#agregar un index dentro del valor de la variable.
#Este ejercicio nos arroja: T
#texto = "Este es el texto de Federico"

#resultado = texto[2].upper()

#print(resultado)
#-------------------------------------------------------------------------
#EJEMPLO 5 MÉTODO LOWER
#Este método es el caso contrario, nos ayuda a transformar tecxto a minúsculas
#El resultado de este ejercicio es: este es el texto de federico
#texto = "Este es el texto de Federico"

#resultado = texto.lower()

#print(resultado)
#-------------------------------------------------------------------------
#EJEMPLO 6 MÉTODO SPLIT
#Este método SEPARARÁ nuestra STRING y los va a GUARDAR dentro de una
#LISTA
#El resultado de esto es una lista:
#['Este', 'es', 'el', 'texto', 'de', 'Federico'] 
#Como vemos, ha descompuesto nuestra string en varias strings.
#Esto es DEBIDO a que toma como SEPARADOR los ESPACIOS VACÍOS. Esto es lo
#Que Python hace por defecto; pero si nosotros ponemos entre los PARÉNTESIS
#Un elemento, Python TOMARÁ este elemento como SEPARADOR, como en el siguiente
#ejemplo, la t (obviamente dentro del paréntesis y entre COMILLAS)
#El resultado de este ejercicio es la lista:
#['Es', 'e es el ', 'ex', 'o de Federico']
#texto = "Este es el texto de Federico"

#resultado = texto.split("t")

#print(resultado)
#---------------------------------------------------------------------
#EJEMPLO 6 MÉTODO JOIN
#Este método nos permite UNIR
#El método join trabaja CON LISTAS
#Aquí vamos a unir los elementos de una lista en una STRING.
#El resultado de esto es: Aprender Python es genial
#Esto es debido a que la variable E las une, y la variable e es 
#UN ESPACIO
#a = "Aprender"
#b = "Python"
#c = "es"
#d = "genial"
#e = " ".join([a,b,c,d])
#print(e)
#-----------------------------------------------------------------------
#Ejemplo 7
#Este ejemplo es de la misma naturaleza que el anterior, solamente que la
#variable e es un - por lo que las variables estarán UNIDAS por un -
#El resultado de este ejercicio es:
#Aprender-Python-es-genial
#a = "Aprender"
#b = "Python"
#c = "es"
#d = "genial"
#e = "-".join([a,b,c,d])
#print(e)
#---------------------------------------------------------------------
#Ejemplo 8 MÉTODO FIND 
#El método find es exactamente igual que el método index. 
#Find busca un determinado caracter dentro de la string.
#Este ejercicio nos arroja: 1 
#Ya que está en el índice 1.
#La ÚNICA diferencia entre este método e index es que cuando con find buscas
#un caracter que NO EXISTE dentro de la string, en vez de arrojarte error,
#como es que lo haría index, te arrojará: -1
#esto es lo que find arroja cuando NO encuentra un caracter.
#texto = "Este es el texto de Federico"

#resultado = texto.find("s")

#print(resultado)
#------------------------------------------------------------------------
#Ejemplo 9 MÉTODO REPLACE
#Este método TOMA un fragmento de nuestro texto y lo REEMPLAZA por OTRO.
#Este método NECESITA PARÁMETROS entre paréntesis (2 parámetros)
#El PRIMERO es el texto que deseamos ELIMINAR
#El SEGUNDO es el texto con el que queremos REEMPLAZAR.
#El resultado de este ejercicio es: Este es el texto de todos
#texto = "Este es el texto de Federico"

#resultado = texto.replace("Federico", "todos") 

#print(resultado)
#-------------------------------------------------------------------------
#También podemos hacer esto, reemplazando CARACTERES específicos y 
#REEMPLAZARLOS por otros.
#El resultado de este sub-ejercicio es:
#Estx xs xl txxto dx Fxdxrico
#texto = "Este es el texto de Federico"

#resultado = texto.replace("e", "x") 

#print(resultado)




#-------------------------------------------------------------------------
#EJERCICIO DE PRUEBA, REEMPLAZAMOS 4 VALORES DE UN TEXTO POR OTROS, CREANDO
#PRIMERO UNA VARIABLE QUE USA REPLACE PARA REEMPLAZAR 2 VALORES
#LUEGO IMPRIMIMOS LA SEGUNDA VARIABLE QUE CONTIENE LOS 2 VALORES REEMPLAZADOS
#Y REEMPLAZAMOS LOS OTROS 2 VALORES RESTANTES. CABE RESALTAR QUE NO PODEMOS
#O NO ENCONTRAMOS LA FORMA DE IMPRIMIR EN UNA MISMA SENTENCIA, EL REEMPLAZO 
#DE 4 VALORES A LA VEZ. TUVIMOS QUE DIVIDIRLO.
#texto = "Si la implementación es difícil de explicar, puede que sea una mala idea."
#texto2 = texto.replace("difícil", "fácil")
#print(texto2.replace("mala","buena"))


'''
--  slicing
En el slicing de una cadena en Python, la notación general es [start:stop:step]. Aquí hay una explicación de cada posición:

start: El índice de inicio del subconjunto de la cadena que estás seleccionando. Si no se proporciona, se asume 0 (el principio de la cadena).

stop: El índice de fin del subconjunto de la cadena que estás seleccionando. Este índice no se incluirá en el resultado. Si no se proporciona, se asume la longitud total de la cadena (el final de la cadena).

step: El tamaño del paso entre los elementos seleccionados. Si no se proporciona, se asume 1 (selecciona cada elemento).

Por ejemplo:

cadena[1:5]: Selecciona los elementos desde el índice 1 hasta el 4 (no incluido), es decir, los elementos en las posiciones 1, 2, 3.

cadena[:5]: Selecciona los elementos desde el principio hasta el 4 (no incluido), es decir, los elementos en las posiciones 0, 1, 2, 3.

cadena[2:]: Selecciona los elementos desde el índice 2 hasta el final de la cadena.

cadena[::2]: Selecciona cada segundo elemento desde el principio hasta el final.

cadena[::-1]: Invierte la cadena.
'''