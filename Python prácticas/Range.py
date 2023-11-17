'''
Ahora veremos rangos, que estos nos sirven para iterar sobre un elemento sin necesidad
de una lista o una variable
-----------------------------------------------------------------------------------------
'''

''' 
EJEMPLO 1

En los anteriores ejemplos, hacíamos una lista con los ELEMENTOS necesarios 
para que iterara el loop:
'''
'''
lista = [1,2,3,4]

for numero in lista:
    print(numero)


Lo anterior nos daba
1
2
3
4

--------------------------------------------------------------
'''

'''
-- EJEMPLO 2 RANGO (range) 
Ahora a la lista, no la vamos a necesitar, y lo haremos directamente en el loop

- La función rango lleva dentro de sus paréntesis EL VALOR DEL RANGO queremos ITERAR. 
este rango va desde el 0 hasta el 5 (recordar que comienza desde el 0)

- El siguiente código nos imprimirá los números del 0 al 4 (ya que NO establecimos desde DÓNDE comenzar, así que
iteró desde el 0. NOTA IMPORTANTE SIEMPRE SE COMERÁ EL ÚLTIMO NÚMERO, ya que funciona similar como index, ASÍ QUE, queremos
iterar del 0 al 30, tendríamos que poner en el paréntesis 31)


for numero in range(5):
    print(numero)

- Lo anterior imprimió

>>0
>>1
>>2
>>3
>>4

- Ahora, lo haremos con un rango INICIAL y un RANGO DESTINO, esto nos
    imprimirá desde el 1 HASTA EL 4 (RECUERDA QUE RANGO SE COME EL ÚLTIMO NÚMERO)
'''
'''
--- EJEMPLO 3 rango con DOS números 

for numero in range(1,5):
    print(numero)

1
2
3
4   
    
'''

'''

-- EJEMPLO 3 RANGO (range) con TRES números

- El tercer número sirve para decirle a Python CADA CUÁNTOS números SALTAR.

- NOTE IMPORTANTE!, range NO RECIBE FLOATS en NINGUNO de sus parámetros.


- En este ejemplo, nos contará DEL 20 al 31 y se saltará CADA 3 NÚMEROS (contará de 3 en 3)


for numero in range (20,31,3):
    print(numero)
    
Esto nos dió:
    
>>20
>>23
>>26
>>29

'''    

'''
-- EJEMPLO 4 

- Los range también podemos usarlos FUERA de los loops, como en los siguientes casos.

- Por ejemplo, tenemos que hacer una lista que vaya del 1 al 100. Tradicionalmente lo haríamos 
    De UNO POR UNO, pero con los range no tiene porqué ser así.
    
- En este caso hacemos una lista del 1 al 100, pero usando la función range, HACIÉNDOLE CASTING (convertirla) 
    y transformándo el range en UNA LISTA.


lista = list(range(1,101))
print(lista)

>> Lo anterior nos arroja una lista del 1 al 100

'''

'''

PRÁCTICA 1 RANGO

Creamos una LISTA formada por todos los números desde el 2500 HASTA el 2585. Almacenamos esa lista en la
variable mi_lista



mi_lista = list(range(2500,2586))
print(mi_lista)

'''

'''

Práctica 2 rango

- Esta vez utilizamos rango para crear una lista que cuente los MÚLTIPLOS de 3 (de 3 en 3) hasta el 300 (ponemos 301 para que lo cuente)

mi_lista = list(range(3,301,3))
print(mi_lista)

>>> Esto nos da como resultado una lista que cuenta de 3 en 3 hasta el 300.

'''
'''
Práctica rango 3:

- INTENTO 1

suma_cuadrados = []
lista = list(range(1,16))

for numero in lista:
    numero = numero ** 2
    suma_cuadrados.append(numero)
print(int(suma_cuadrados))

'''
'''

Calcula la suma de los cubos de los números del 1 al 10 y almacena
el resultado en una variable llamada suma_cubos.
Recuerda, para cada número del 1 al 10, eleva ese número al cubo y suma los resultados 
para obtener suma_cubos. ¡Inténtalo!

'''
'''
INTENTO SOLO EXITOSOOOOOOOO

-- En este ejercicio de práctica, teníamos que almacenar en una variable llamada suma_cuadrados
    la suma de los cuadrados del 1 al 15.
    
- Para lograr esto, establecimos suma_cuadrados en 0, esto ya que NOS PEDÍAN EL RESULTADO EN INTEGER (no en lista) Como ESTÁ en 0, 
    nos sirve para ALMACENAR la SUMA ACUMULATIVA (Esto quiere decir que nos va a sumar CADA CUADRADO, con EL VALOR que haya tenido 
    en el ANTERIOR cuadrado, por ejemplo, al inicio, suma_numeros vale 0, luego cuadrados 1 al cuadrado es 1. EN EL SIGUIENTE, suma_numeros vale 1 y el siguiente cuadrado es 4, y 4 + 1 es 5.
    luego, el el siguiente 3 al cuadrado vale 9, mas 5 del valor de suma_numeros da como resultado 14, y as+o sucesivamente. A ESTO SE LE LLAMA SUMA ACUMULATIVA.)
    
- Luego for in range(1,16) recorre del 1 al 15 (no olvidar que no incluye el 16)

- cuadrado = numero ** 2 eleva al cuadrado el número ACTUAL (cada iteración la va sumando) del range      

suma_cuadrados = 0

for numero in range(1,16):
    cuadrados = numero ** 2
    suma_cuadrados = cuadrados + suma_cuadrados 
print(suma_cuadrados)

'''
'''

suma_cuadrados = 0

for numero in range(1,16):
    cuadrados = numero ** 2
    suma_cuadrados = cuadrados + suma_cuadrados 
    print(suma_cuadrados)
'''
    
    
'''
Ejercicio suma de pares 1 enfoque con módulo

num2 = 10
num2 = float(num2)
print(num2)
'''
'''
suma_pares = 0

for numero in range(1,51):
    if numero % 2 == 0:
        suma_pares += numero
    
print(suma_pares)
'''

'''
Ejercicio de suma pares 1 enfoque range.

suma_pares = 0

for numero in range (2,51,2):
    suma_pares += numero
print(suma_pares)

'''
    
    
''' 
 
Tenemos que crear un bucle while que cuente del 0 al 20, pero solo los que son múltiplos de 3.

'''
'''
este ejercicio imprime los números múltiplos de 3 del 0 al 20 con bucle while.

multiplos = 0

while multiplos <= 20:
    if multiplos % 3 == 0:
        print(multiplos)
    multiplos += 1
'''

'''

numeros = range(10,31)

for numero in numeros:
    if numero % 2 == 1:
        print(numero)
        print(type(numero))
'''
'''
Mismo ejercicio que el anterior, pero más compacto
for numero in range(10,31):
    if numero % 2 == 1:
        print(numero)
'''


        
    
    
    
    
    
    
   
    