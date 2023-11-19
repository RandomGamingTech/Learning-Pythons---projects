#Ejemplo 1
#Los operadores lógicos nos sirven para hacer DOS O MÁS COMPARACIONES 
#Al mismo tiempo.
#En este ejemplo queremos que se almacene en UNA SOLA VARIABLE estas dos
#comparaciones:
#4 < 5
#5 < 6

#Lo anterior sería una comparación DIRECTA donde ponemos los tres valores.
#Lo siguiente sería una comparación DIRECTA donde ponemos los tres valores
#Lo siguiente NO SIEMPRE funcionará bien, y NO ES TAN LEGIBLE.
 
#mi_bool = 4 < 5 < 6
#print(mi_bool)
#>>>True

#----------------------------------------------------------------------------------------------
#Ejemplo 2 Operador and
#Para resolver esto y que además sea MÁS LEGIBLE es a través de los OPERADORES LÓGICOS
#El siguiente ejemplo tenemos el mismo caso, pero esta vez mucho MÁS LEGIBLE.
#NOTE si bien 4 SÍ es MENOR a 5, 5 NO es MAYOR a 6. Entonces el resultado de esta comparación nos
#dará False, debido a que para que una comparación nos de True TODAS LAS COMPARACIONES TIENEN QUE SER 
#VERDADERAS!!!!!!!!!

#mi_bool = 4 < 5 and 5 > 6 
#print(mi_bool)
#>>>False

#Por ejemplo, si la segunda comparación fuera que 4 es MENOR a 5 y 5 es IGUAL a 2+3 entonces ahí SÍ nos daría
#True, ya que AMBAS comparaciones son verdaderas (+ * + = +)

#mi_bool = 4 < 5 and 5 == 2+3 
#print(mi_bool)
#>>>True

#NOTE también podemos poner entre PARÉNTESIS nuestras OPERACIONES para que se vea más LEGIBLE.
#------------------------------------------------------------------------------------------------------
#Ejemplo 3 Comparaciones de diferentes TIPOS.
#El resultado del siguiente ejercicio es OBVIAMENTE True.

#mi_bool = (55 == 55) and ("perro" == "perro") 
#print(mi_bool)
#>>>True

#------------------------------------------------------------------------------------------------------
#Ejemplo 4 Operador or
#Nos sirve para verificar si una comparación es IGUAL a otra
#NOTE CON ESTE OPERADOR, si la primera comparación es False, pero la SEGUNDA es VERDADERA (o la que sea que fuera)
#Nos dará True, a diferencia que con el operador and
#Esto porque queremos saber si UNA U OTRA es VERDADERA (or).

#mi_bool = 1 == 10 or 3 == 3
#print(mi_bool)
#>>>True

#La única forma en la que or puede resultar FALSO es cuando TODAS LAS COMPARACIONES son FALSAS.
#mi_bool = 1 == 10 or 3 == 30
#print(mi_bool)
#>>>False

#-----------------------------------------------------------------------------------------------------------------------
#Ejemplo 5 Buscar VARIAS palabras A LA VEZ con and.
#Aquí buscamos si la palabra frase está en la variable texto, esto nos
#arrojará True porque efectivamente, está texto.
#texto = "esta frase es breve"
#mi_bool = "frase" in texto
#print(mi_bool)
#>>>True

#Pero para buscar VARIAS PALABRAS A LA VEZ HACEMOS LO SIGUIENTE:
#Aquí buscamos si ambas palabras están en la variable texto, y como AMBAS son 
#verdaderas, nos dará True
#texto = "esta frase es breve"
#mi_bool = ("frase" in texto) and ("breve" in texto)
#print(mi_bool)
#>>>True

#Como bien sabemos el comportamiento del operador and, si buscamos una palabra que NO ESTÁ
#en la variable, aunque haya una que SÍ esté, nos dará False.
#texto = "esta frase es breve"
#mi_bool = ("frase" in texto) and ("python" in texto)
#>>>False

#---------------------------------------------------------------------
#Ejemplo 6 Operador not
#Nos permite NEGAR el VALOR de una variable.
#La siguiente comparación debería darnos True, pero como la estamos negando con el operador not
#Esto nos CONVERTIRÁ True en False.
#NOTE en algunas bibliotecas de Python es OBLIGATORIO usar PARÉNTESIS en las comparaciones.

#mi_bool = not ("a" == "a")
#print(mi_bool)
#>>>False

#Ahora en este caso, como estamos haciendo una doble negación (ya que usamos != para decir que a NO es IGUAL
# a a, entonces nos da Falso, y como not niega Falso, entonces es True)
#mi_bool = not ("a" != "a")
#print(mi_bool)
#>>>True


 
mi_bool = 1 == 10 or 3 == 3
print(mi_bool)