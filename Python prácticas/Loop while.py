#EJEMPLO 1 
#Aquí en este ejemplo le pedimos a Python que MIENTRAS monedas sea mayor a 0, imprima "Tengo {} de monedas"
#Como aquí monedas SÍ es mayor a 0, el código se ejecutará INFINITAS VECES.
#Esto no se detendrá en otros IDE hasta que cierres el programa o hasta que reinicies el computador. Aquí en VSC aplanamos CTRL + C y listo, SE DETIENE.

#monedas = 5

#while monedas > 0:
    #print(f"Tengo {monedas} monedas")
    
#Para arreglar lo anterior, entonces ahora lo que hacemos es establecer que por CADA ITERACIÓN que el bucle de, le reste -1 a la variable monedas.
#Esto hará que llegue a un punto donde MONEDAS llegará a 0 y la condición se DEJE de CUMPLIR, por lo que el bucle while se DENTENDRÁ.

#NOTE aquí usamos el signo -= que es una abreviatura de monedas = monedas - 1 
#O sea, que -= significa: monedas ES IGUAL a monedas -1

#monedas = 5

#while monedas > 0:
    #print(f"Tengo {monedas} monedas")
    #monedas -= 1

#Aquí por cada iteración restó -1 a monedas hasta que llegó a 0 y ahí paró. En otras palabras, MIENTRAS monedas sea MAYOR a 0 IMPRIME y RESTA a monedas -1.

#>>Tengo 5 monedas
#>>Tengo 4 monedas
#>>Tengo 3 monedas
#>>Tengo 2 monedas
#>>Tengo 1 monedas

#También podríamos poner un bloque else y esto imprimiría "no tengo más dinero". Ya que recoje el resultado SOBRANTE.
      
#monedas = 5

#while monedas > 0:
    #print(f"Tengo {monedas} monedas")
    #monedas -= 1
#else:
    #print("No tengo más dinero")

#------------------------------------------------------------------------------------------------------------------------
#EJEMPLO 2 LOOP while + input
#En el anterior ejemplo NOSOTROS SÍ DEFINIMOS hasta CUÁNDO se iba a ejecutar el loop while (le restábamos -1 a cada iteración)
#Pero este loop brilla por ejemplo cuando el USUARIO va a ingresar datos.
#En el siguiente ejemplo, MIENTRAS que la respuesta sea s, el bucle CONTINUARÁ REPITIENDO la impresión de "Quieres seguir? " hasta que 
#el resultado (else) sea DIFERENTE a S, entonces ahí imprimirá lo que tenemos en el bloque else (Gracias). 
#NOTE OJO QUE TENEMOS QUE PONER COMO VALOR LA LETRA O NÚMERO O LO QUE SEA QUE QUERAMOS EVITAR (ya que el bucle se activará con la letra S, pero
# se pausará para que la variable SE ACTUALICE CON EL INPUT.)

#respuesta = "s"

#while respuesta == "s":
    #respuesta = input("quieres seguir? (s/n): ")
#else:
    #print("Gracias")
#>>#Esto nos imprimirá "quieres seguir? (s/n): " TODAS LAS VECES QUE PONGAMOS S hasta que pongamos CUALQUIER OTRA COSA (else) y nos imprimirá 
#>>#Gracias.  

#----------------------------------------------------------------------------------------------------------------------------------------
#EJEMPLO 3 PALABRAS CLAVES PARA LOOPS (pass)
#pass nos ayudará a que el loop NO HAGA NADA (lo pase). 
#¿Para qué nos sirve?
#Pass es un PLACEHOLDER que nos ayuda a EVITAR errores de sintaxis cuando tenemos una línea de código que NO REQUIERE NINGUNA ACCIÓn, y queremos SEGUIR}
#programando, por lo que nos vamos y dejamos INCOMPLETO ese bloque y seguimos con lo nuestro, SIN QUE GENERE error de sintaxis. 
#Esto solamente SIRVE para que no se vea la linea roja, no tiene utilidad alguna. Solamente nos sirve como un MARCADOR VISUAL que no HEMOS terminado el bloque de código.

#respuesta = "s"

#while respuesta == "s":
    #print("hola mundo")  
    #pass
#print("Hola mundo")     

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#EJEMPLO 4 Palabra clave break
#NOS SIRVE PARA INTERRUMPIR LA ITERACIÓN ACTUAL en la que LA PONGAMOS y nos SACA DIRECTAMENTE del LOOP.
#El siguiente código nos imprime el NOMBRE que ingresemos LETRA POR LETRA.
#¿Hay alguna forma de hacer el deje de imprimir en algún momento las letras del nombre?
#Para eso usamos la palabra clave break.
#Aquí la palabra break, SI letra llega a ser IGUAL a "i" se interrumpirá el loop.

#nombre = input("Tu nombre: ")

#for letra in nombre:
    #if letra == "i":
        #break
    #print(letra)
    
    
            
#>>#El resultado de esto es que el NOMBRE ingresado se DEJA de imprimir LETRA por letra cuando APAREZCA una i.    

#-----------------------------------------------------------------------------------------------------------------------------------------
#EJEMPLO 5 Palabra clave continue
#Esta palabra INTERRUMPE la ITERACIÓN donde la pongamos pero NO INTERRUMPE el loop, SINO que VUELVE al COMIENZO y continúa con la ITERACIÓN siguiente.
#Esto por ejemplo, si escribimos en el type David, se SALTARÁ la i y CONTINUARÁ con las DEMÁS LETRAS.
#nombre = input("Tu nombre: ")

#for letra in nombre:
    #if letra == "i":
        #continue
    #print(letra)
    

#>>#El resultado de esto, es que si escribimos un nombre que contenga una i, interrumpirá la secuencia y CONTINUARÁ imprimiendo lo demás que NO CONTENGA i.

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#respuesta = "s"

#while respuesta == "s":
    #respuesta = input("quieres seguir? (s/n): ")
#else:
    #print("Gracias")
#>>#Esto nos imprimirá "quieres seguir? (s/n): " TODAS LAS VECES QUE PONGAMOS S hasta que pongamos CUALQUIER OTRA COSA (else) y nos imprimirá 
#>>#Gracias.

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#EJERCICIOS DE LOOPS WHILE

#Ejercicio 1 CUIDADO CON EL PRINT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#NOTA SOBRE EL FLUJO DEL DOCUMENTO: Hay que tener cuidado dónde ponemos un print. Por ejemplo, cuando ponemos el print aquí DESPUÉS de la INSTRUCCIÓN DEL BUCLE
#Nos imprimirá desde UN NÚMERO ANTES DEL VALOR DE LA VARIABLE!!! Esto debido a que COMIENZA A RESTAR DIRECTAMENTE DESDE EL 10!!! y 10-1 da 9 y así, hasta que el resultado sea 0
#YA QUE PRINT RECOGERÁ EL SOBRANTE

#numero = 10

#while numero > 0:
    #numero -= 1
    #print(numero)

#En este mismo caso, nosotros ponemos el print ANTES de la instrucción, el resultado es que PRIMERO va a IMPRIMIR el VALOR de la variable y LUEGO la respectiva instrucción, que en este caso, es 
#una resta (-1 por cada iteración)
#Esto nos va a imprimir DESDE EL 10 HASTA EL 1. Nos imprime hasta el 1, ya que print no recoge el DATO SOBRANTE.

#numero = 50

#EJERCICIO 2 PYTHON LOOP WHILE

#while numero >= 0:
    #if numero % 5 == 0:
        #print(numero)
    #numero -= 1 #nota, aquí la identación para que nos IMPRIMA 0, TIENE QUE ESTAR A LA ALTURA DEL IF, si no NO NOS IMPRIMIRÁ !!!INFINITAMENTE!!! el 50, ya que el NO TOMARÁ EN CUENTA EL -1, solo el print, y como el número
                #50 SIEMPRE será mayor a 0, POR ESO nos imprimirá el 50. LA IDENTACIÓN DE LA RESTA Y LA SUMA, TIENE QUE ESTAR A LA ALTURA DE LA ORDEN.
                
#Ejemplo CHAT GPT (LO RESOLVIMOS POR NUESTRA CUENTA)
#numeros = 100

#while numeros >= 0:
    #if numeros % 2 == 0:
        #print(numeros)
    #numeros -= 10

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
EJEMPLO NÚMERO 2 CHAT GPT
    
numeros = 1

while numeros <= 10:
    if numeros % 3 == 0:
        print(numeros)
    numeros += 1

''' 
'''
EJEMPLO NUMERO 3
numeros = 20

while numeros >= 0:
    if numeros % 3 == 0:
        print(numeros)
    numeros -= 1
'''
'''
EJERCICIO 4
numeros = 2

while numeros <= 50:
    if numeros % 2 == 0:
        print(numeros)
    numeros += 1 
'''    
'''
EJERCICIO 5 
Aquí almacenamos los números en una variable con una lista vacía. Al final la imprimimos.
numeros = 10
lista = [] 

while numeros >= 0:
    if numeros % 2 == 0:
        lista.append(numeros)
    numeros -= 2
print(lista)
'''
'''
numero = 10

while numero >= 0:
    print(numero)
    numero -= 1 
    
'''
'''
 Ejemplo número 6
numero = 10

while numero >= 0:
    if numero != 0:
        print(numero)
    numero += 1
''' 

'''
numeros = 15

while numeros >= 0:
    if numeros < 10:
        break
    print(numeros)
    numeros -= 1
'''
    
                

    

        
  
    
    

    