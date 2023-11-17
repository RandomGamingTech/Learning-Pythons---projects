#Primer ejemplo
#mi_texto = "Esta es una prueba"
#resultado = mi_texto[1]
#print(resultado)
#Obtenemos s
#------------------------------------------------------------------------
#Segundo ejemplo: INDEX NEGATICO BUSCAR LETRAS AL REVES (OBTENER LA ÚLTIMA LETRA DE UNA CADENA)!!!!!
#mi_texto = "Esta es una prueba"
#resultado = mi_texto[-4]
#print(resultado)
#Obtenemos u
#-----------------------------------------------------------------------
#Tercer ejemplo:
#Con esta sintaxis podemos buscar en qué índice se encuentra una letra dentro
#de la string. TAMBIÉN PODEMOS BUSCAR PALABRAS CON ESTE MÉTODO y Python nos dirá
#en qué índice comienza la palabra.
#NOTA: PYTHON es sensible a los errores de tipográficos, por lo que si buscamos
#una palabra dentro de una string y la escribimos diferente a como se encuentra 
#alojada en la variable, entonces nos arrojará ERROR.
#TAMBIÉN ES SENSIBLE A MAYÚSCULAS, por lo que también arrojará error si
#no buscamos en el formato correcto.
#mi_texto = "Esta es una prueba"
#resultado = mi_texto.index("PRUEBA")
#print(resultado)
#aquí nos arroja un error debido a que lo buscamos en MAYÚSCULAS, si lo hubiéramos buscado
#tal cuál viene en la string, o sea, en minúsculas, hubieramos obtenido 12 porque ahí comienza
#la palabra prueba.
#------------------------------------------------------------------------
#Cuarto ejemplo:
#Qué pasa si buscamos una letra que se REPITE varias veces?
#mi_texto = "Esta es una prueba"
#resultado = mi_texto.index("a")
#print(resultado)
#Esto nos arrojará 3, ya que index buscará de derecha a izquiera y se 
#detendrá cuando encuentre EL PRIMER RESULTADO.
#----------------------------------------------------------------------
#Quinto ejemplo
#Podemos decirle a Python desde DONDE buscar, de la siguiente manera:
#mi_texto = "Esta es una prueba"
#resultado = mi_texto.index("a",5)
#print(resultado)
#Aquí nos arroja como resultado 10, debido a que Python comenzó a contar
#desde el 5to (recuerda que Python cuenta desde 0) y comenzó a buscar desde ahí, dándonos 10.
#--------------------------------------------------------------------------
#Sexto ejemplo
#También podemos decirle a Python HASTA DONDE busque, agregando un tercer
#caracter:
#Si le pedimos a Python que busque dentro de un rango y el último caracter del
#rango especificado contiene la letra o palabra solicitada, nos arrojará ERROR.
#mi_texto = "Esta es una prueba"
#resultado = mi_texto.index("a",5,10)
#print(resultado)
#Esto nos da error.
#--------------------------------------------------------------------------
#Séptimo ejemplo
#rindex este método es parecido a index pero busca de derecha a izquierda
#mi_texto = "Esta es una prueba"
#resultado = mi_texto.rindex("a")
#print(resultado)
#Nos arroja 17 ya que BUSCA de derecha a izquierda, contando igualmente como 
#0 la letra "E" y nos da la posición de la primera letra "a" de la DERECHA.






