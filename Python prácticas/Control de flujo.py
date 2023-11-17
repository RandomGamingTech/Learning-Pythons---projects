#CONTROL DE FLUJO (if, elif, else)
#Ejemplo 1 if
#Aquí imprimimos es correcto, SI 10 es MAYOR a 9
#Como el resultado es True, Python nos imprime Es correcto
#if 10 > 9: 
    #print("Es correcto")
#>>>Es correcto

#---------------------------------------------------------------------
#Aquí agregamos una variable True
#Verificamos directamente x y como ES True, entonces nos imprime "Es correcto"
#recordar que if lo que hace es verificar si una variable es Truem y como aquí
#le damos directamente el valor True, nos imprime lo solicitado.

#x = True

#if x: 
    #print("Es correcto")
#>>>Es correcto

#--------------------------------------------------------------------------------------
#En este ejemplo, como claramente 5 NO es igual a 2, Python ignora el resultado y no imprime
#NADA.
#if 5 == 2:
    #print("Es correcto")
    
#------------------------------------------------------------------------------------------------------    
#Ejemplo 2 else    
        
#Ahora, agregamos luego de if, un else, que quiere decir SI NO, (si no se cumple la condición) que
#imprima no es correcto.

#if 5 == 2: 
    #print("Es correcto")
#else: 
    #print("No es correcto")
#>>>No es correcto           
    
#--------------------------------------------------------------------------------------------------        
#El siguiente código tiene una variable establecida en "perro", le pedimos a Python que SI
#mascota es "gato" imprima que "Tienes un gato", SI NO ES ASÍ, que imprima "No sé qué animal tienes"
#Como no tiene un "gato" como mascota, entonces imprime "No sé qué animal tienes"
#mascota = "perro"

#if mascota == "gato":
    #print("Tienes un gato")
#else:
    #print("No sé qué animal tienes")
#>>>No sé qué animal tienes     

#----------------------------------------------------------------------------------------------------------
#Ejemplo 3 elif
#Ahora agregaremos DIFERENTES CONDICIONES.
#Lo que hacemos aquí es EN CASO DE QUE.
#Aquí como agregamos la condición elif que ENCASO DE que mascota == "perro", nos imprima "tienes un perro".

#mascota = "perro"

#if mascota == "gato":
    #print("Tienes un gato")
#elif mascota == "perro":
    #print("Tienes un perro")
        
#else:
    #print("No sé qué animal tienes")
    
#>>>Tienes un perro

#-------------------------------------------------------------------------------------------------------------------    
#Podemos agregar TANTOS elif como queramos.
#Aquí cambiamos el valor de la variable por pez.
#Ahora añadimos la condición de que EN CASO DE que mascota sea IGUAL a PEZ, imprima "Tienes un pez"
#mascota = "pez"

#if mascota == "gato":
    #print("Tienes un gato")
#elif mascota == "perro":
    #print("Tienes un perro")
#elif mascota == "pez":
    #print("Tienes un pez")         
#else:
    #print("No sé qué animal tienes")
#>>>"Tienes un pez"

#-----------------------------------------------------------------------------------------------------------------------
#Podemos ir ANIDANDO elementos if
#Siempre que RESPETEMOS la JERARQUÍA de las TABULACIONES podemos anidar más if dentro de un if.
#Aquí preguntamos a Python por DOS condiciones mediante un if padre y un if anidado. Y si no, que imprima "no aprobado".
#En este caso como las condiciones SÍ se cumplen, nos imprime "Eres menor de edad" y "Aprobado"

#edad = 16
#calificacion = 9


#if edad < 18:
    #print("Eres menor de edad")
    #if calificacion >= 7:
        #print("Aprobado") #NOTE IMPORTANTE!! Cuando anidamos un if, el print, o la consecuencia, DEBE TENER SANGRÍA!!!!, de lo contrario, no servirá.
    #else:
        #print("No aprobado") #Aquí, si la calificación es menor a 7, directamente te proporciona el resultado "No aprobado"
#else: 
    #print("Eres adulto")
        



#--------------------------------------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 2 DE PRÁCTICA EN UDEMY
#edad = 16
#tiene_licencia = False

#if edad >= 18 and tiene_licencia:
    #print("Puedes conducir")
#elif edad >= 18 and not tiene_licencia:
    #print("No puedes conducir. Debes tener 18 años y contar con una licencia")
#else:
    #print("No puedes conducir. Debes ser mayor de 18 años y tener una licencia")      

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#EJERCICIO 3 DE PRÁCTICA UDEMY

habla_ingles = True
sabe_python = False

if habla_ingles and sabe_python:
    print("Cumples con los requisitos para postularte")
elif not habla_ingles and not sabe_python:
        print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif sabe_python and not habla_ingles:  
 print("Para postularte, necesitas tener conocimientos de inglés")
else:
    print("Para postularte, necesitas saber programar en Python")    
    
