'''
-- EJEMPLO 1 CASTING CON LISTA

- Nosotros podemos combinar DOS elementos de DOS LISTAS diferentes, con la función ZIP, la cuál nos 
    permite combinar EN PARES (par en cada tuple) los elementos de ambas listas encerrado en un casting de lista.



nombres = ["Ana", "Hugo", "Valeria"]
edades = [65, 29, 42]

combinados = list(zip(nombres,edades))

print(combinados)

>>[('Ana', 65), ('Hugo', 29), ('Valeria', 42)]

- Si por ejemplo agregamos un elemento más a cualquiera de estas listas, por ejemplo, agregamos 55
    a la lista de edades, NO PASARÁ NADA EXTRA, debido a que ZIP solamente LLEGA HASTA EL LARGO DE la lista MÁS CORTA.
    por lo que basado en la lista más corta, creará los pares de TUPLES.

'''

'''

-- EJEMPLO 2 ¿Qué pasa si agregamos otro elemento a una lista y la dejamos desigual?

nombres = ["Ana", "Hugo", "Valeria"]
edades = [65, 29, 42, 55]

combinados = list(zip(nombres,edades))

print(combinados)

[('Ana', 65), ('Hugo', 29), ('Valeria', 42)]

'''

'''
-- EJEMPLO 3 COMBINAR MÁS DE DOS LISTAS

- Con la función ZIP podemos combinar más de dos listas.
    Esto nos genera tuples MÁS LARGOS (tuples de 3 elementos). 


nombres = ["Ana", "Hugo", "Valeria"]
edades = [65, 29, 42]
ciudades = ["Lima", "Madrid", "Mexico"]

combinados = list(zip(nombres,edades, ciudades))

print(combinados)


>>[('Ana', 65, 'Lima'), ('Hugo', 29, 'Madrid'), ('Valeria', 42, 'Mexico')]

'''

'''
-- EJEMPLO 4 
    - Esta función nos SIRVE MUCHO cuando por ejemplo queremos crear un LOOP que tenga TODOS los elementos
    de nuestras LISTAS.
    
    Con esto hemos creado UN SISTEMA que NO NECESITA que estemos BUSCANDO los INDICES de los elementos. 
'''
'''
nombres = ["Ana", "Hugo", "Valeria"]
edades = [65, 29, 42]
ciudades = ["Lima", "Madrid", "Mexico"]

combinados = list(zip(nombres,edades,ciudades))

for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")
    '''

'''

-- PRACTICA POR NUESTRA CUENTA 1. 
    - El siguiente código NO FUNCIONA, ya que trata de restar AMBOS elementos de la lista, y esto 
        NO SERÁ POSIBLE ya que la función ZIP COMBINA ELEMENTOS de DOS o MÁS ITERABLES. Y SI UNO DE LOS ITERABLES
        es MÁS CORTO que el OTRO, ZIP se DETENDRÁ cuando el ITERABLE MÁS CORTO, SE AGOTE
    - Por lo que aquí, si restamos 51 - 1 (numero1 - numero) nos dará 50, PERO DE AHÍ YA NO SALDRÁ MAS QUE 50 debido a que EL 
        ITERABLE MÁS CORTO SE AGOTÓ.
    
numeros = list(range(1,50))
numeros2 = list(range(51,100,))

resta = list(zip(numeros,numeros2))

for numero,numero1 in resta:
    print(f"Este numero: {numero1} menos este otro {numero} da {numero1 - numero}")
    
    '''




'''
-- PRACTICA POR NUESTRA CUENTA 2

Crearemos un bucle que sume solamente los numeros PARES en una lista usando range, zip y loop.


'''


        
'''
-- PRACTICA 1 ZIP

-   En este ejemplo, tenemos que imprimir tanto la capital como el país haciendo un ZIP de ambas listas que contienen capitales y paises.
    NOTE recordar que tenemos que PONER LA VARIABLE CON EL ZIP ANTES DEL BUCLE (o después de las listas), si no, NO SERVIRÁ.
    
- Luego creamos nuestra VARIABLE que CONTENDRÁ nuestro ZIP (CON CASTING de LISTA NO OLVIDAR)

- Luego creamos el bucle FOR con el cuál iteramos por CADA CAPITAL Y PAIS de LA VARIABLE ZIP.

-   Creamos un FORMATO que nos da una frase impresa por CADA ITERACIÓN DEL ZIP.

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

frase = list(zip(capitales,paises))

for capital,pais in frase:
    print(f"La capital de {pais} es {capital}")

'''
'''
1: uno / um / one
2: dos / dois / two
3: tres / três / three
4: cuatro / quatro / four
5: cinco / cinco / five 
'''

'''

lista1 = ["uno", "dos", "tres", "cuatro", "cinco"]
lista2 = ["um", "dois", "três", "quatro", "cinco"]
lista3 = ["one", "two", "three", "four", "five"]

numeros = list(zip(lista1,lista2,lista3))

print(numeros)

'''

    
    
