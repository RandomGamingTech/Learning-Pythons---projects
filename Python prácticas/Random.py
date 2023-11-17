'''
-- EJEMPLO 1 randint

    - Las aplicaciones de random tendrán muchas aplicaciones en el mundo de los JUEGOS y en 
        aplicaciones donde necesitamos que el sistema elija algo al azar.

- Randint nos proporcionará un NÚMERO ALEATORIO.

- Primeramente, HAY QUE IMPORTARLO, esto lo hacemos mediante from, mencionando la librería, import y mencionando
    el método que queremos importar.
    
NOTE ES MUY IMPORTANTE TENER EN CUENTA QUE NO DEBEMOS NOMBRAR NUESTRO ARCHIVO IGUAL QUE LAS LIBRERÍAS
QUE VAMOS A IMPORTAR, porque esto generaría una IMPORTACIÓN CIRCULAR. Entonces lo que hacemos es ponerle al archivo 
"Random" con MAYÚSCULA INICIAL.

- Entonces lo que hacemos LUEGO de IMPORTAR nuestra librería y nuestro método, es declarar una variable y como valor, le ponemos
    randint(1,50) proporcionándole un RANGO desde dónde hasta dónde queremos que ESCOJA un NÚMERO ALEATORIO.
    - Cada vez que nosotros IMPRIMAMOS la misma variable con randint NOS ESTARÁ PROPORCIONANDO DIFERENTES NÚMEROS ALEATORIOS.
        Esto sería beneficioso por ejemplo para hacer un sorteo.
        
from random import randint

aleatorio = randint(1,50)

print(aleatorio)

>>Un número aleatorio de entre 1 y 50.        
        
'''

'''
--  EJEMPLO 2, MÉTODO UNIFORM

    - Ahora, en lugar de importar de uno a uno los métodos que necesitamos, vamos a importarlos TODOS.
    
    - Uniform, nos va a dar UN VALOR ALEATORIO, pero esta vez, UN FLOAT dentro del RANGO ESTABLECIDO.
        Cuando lo ejecutemos, nos dará un número con MUCHÍSIMOS decimales, para evitar tantos decimales, podemos usar
        round y establecer cuántos decimales queremos.
    
from random import *

aleatorio = round(uniform(1,5),1)
print(aleatorio)    
    
'''

'''
--  EJEMPLO 3 MÉTODO RANDOM

    - Ahora veremos un tercer método que se llama random, este método NO NECESITA NINGÚN PARÁMETRO, sus paréntesis van VACÍOS.
        y lo que hace random es AUTÉNTICAMENTE ELEGIR un NÚMERO FLOAT entre 0 y 1.
        Esto quiere decir que cada vez que lo ejecutemos, igual como los anteriores, nos dará un número decimal de entre 0 a 1.
    
    - Esto es bueno para trabajar con porcentajes o fracciones.
   
from random import *

aleatorio = random()
print(aleatorio)   
        
'''

'''
--  EJEMPLO 4 MÉTODO CHOICE (para elementos de una lista)

    - choice nos permite trabajar con una selección aleatoria dentro de los elementos de una lista.
    Por ejemplo en esta lista tenemos una lista llamada colores. Con el método choice le pedimos a Python
    que nos ESCOJA un ELEMENTO ALEATORIO dentro de la LISTA.

from random import *

colores = ["azul", "rojo", "verde", "amarillo"]
aleatorio = choice(colores)
print(aleatorio)
    
'''

'''
--  EJEMPLO 5 MÉTODO SHUFFLE

    - Ahora trabajaremos con un método llamado shuffle (en inglés, mezclar).
    Esto sería útil en los juegos de cartas o algo similar.
    
    - En este ejemplo creamos una lista que va del 5 hasta el 50 pasando de a 5 en 5. 
        Entonces, ANTES DEL PRINT, INVOCAMOS EL MÉTODO SHUFLE y mezclamos la lista numeros.
        Entonces cada vez que imprimamos, nos MEZCLARÁ nuestros elementos EN UN ORDEN DIFERENTE.
        
    NOTE el método SHUFFLE es un método que NO PODEMOS almacenar EN UNA LISTA. O sea, genera una modificación
    in situ.        
        
'''

from random import *

numeros = list(range(5,50,5))

shuffle(numeros)

print(numeros)


    


