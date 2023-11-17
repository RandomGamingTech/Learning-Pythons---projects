#EJEMPLO 1 STRINGS SON INMUTABLES
#En el siguiente ejemplo, queremos cambiar la letra C de Carina por K;
#pero Python nos manda error, debido a que los strings NO soportan 
#ASIGNACIÓN de items. 
#Esto nos demuestra que las strings son INMUTABLES en su CONTENIDO y su ORDEN.
#nombre = "Carina"
#nombre[0] = "K"
#print(nombre)
#----------------------------------------------------------------- 
#Actualizar la string por medio de actualizar la variable.
#En este ejemplo, hemos modificado Carina a Karina; pero porque lo 
#HICIMOS a través de una variable. El STRING ORIGINAL, no CAMBIA.
#nombre = "Carina"
#nombre = "Karina"
#print(nombre)
#>>>Karina
#-------------------------------------------------------------------
#EJEMPLO 2
#Podemos concatenar strings
#n1 = "Kari"
#n2 = "na"
#print(n1 + n2)
#-----------------------------------------------------------------
#EJEMPLO 3 
#Los strings son multiplicables
#n1 = "Kari"
#n2 = "na"
#print(n1 * 10)
#>>>KariKariKariKariKariKariKariKariKariKari
#-----------------------------------------------------------------
#EJEMPLO 4
#Una string puede contener VARIAS líneas de código
#Esto se logra mediante la triple comilla (puede ser doble o simple)
#poema = """Mil pequeños peces blancos 
#como si hirviera 
#el color del agua"""
#print(poema)
#>>>Mil pequeños peces blancos 
#>>>como si hirviera
#>>>el color del agua
#-----------------------------------------------------------------
#EJEMPLO 5 CONSULTAR ELEMENTOS.
#Nosotros podemos saber si en una string existe una string existe
#una determinada palabra o caracter (básicamente un sub-string)
#esto lo hacemos mediante in que básicamente es en. La sintaxis 
#traducida sería: imprime agua si está EN poema.
#Esto nos arrojará un True o un False (un boleano) dependiendo si el substring 
#existe dentro de la string.
#poema = """Mil pequeños peces blancos 
#como si hirviera 
#el color del agua"""
#print("agua" in poema) 
#------------------------------------------------------------------
#También podemos preguntarle a Python si una palabra NO se encuentra 
#Dentro de una string agregando not. Como aquí le preguntamos a Python
#Si sol NO está de dentro de poema, nos da como resultado True
#poema = """Mil pequeños peces blancos 
#como si hirviera 
#el color del agua"""
#print("sol" not in poema)
#>>>True
#------------------------------------------------------------------
#En este ejemplo, ocurre lo mismo, pero al revés. Le preguntamos a Python
#Si agua NO está dentro de poema, y como sí está, nos responde False
#poema = """Mil pequeños peces blancos 
#como si hirviera 
#el color del agua"""
#print("agua" not in poema)
#>>>False
#-------------------------------------------------------------------
#Ejemplo 6
#Podemos conocer el LARGO de una string con la propiedad len. El largo
#no es otra cosa el número de caracteres, espacios vacíos y signos.
#CABE RESALTAR QUE AQUÍ NO ES COMO EN INDEX, AQUÍ PYTHO CUENTA DESDE EL 1
#NO DESDE EL 0
#poema = """Mil pequeños peces blancos 
#como si hirviera 
#el color del agua"""
#print(len(poema))
#>>>63
