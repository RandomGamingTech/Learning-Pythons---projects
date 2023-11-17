'''
-- EJEMPLO 1 Método sin enumerador.

    -Creamos una lista donde necesitamos acceder a los índices de los elementos de una lista con los elementos
    que tenemos hasta ahora.
    En este ejemplo necesitaríamos crear otra variable que se llame por ejemplo índice, que comience en 0.
    aquí lo que hacemos es por cada item en la lista, en cada iteración (3 en total) imprimimos índice y item (desde el 0).
    Luego, para que el índice vaya sumando de 1 en 1 (0,1,2) logramos hacerlo sumando 1 con cada iteración declarando que el índice se 
    sume +1 POR CADA ITERACIÓN.
    
    PERO ESTA NO ES LA MEJOR MANERA DE HACERLO.

lista = ["a","b","c"]
indice = 0

for item in lista:
    print(indice,item)
    indice += 1

---------------------------------------------------------------------------------------------------------------------------------------------
'''
'''
-- EJEMPLO 2, numerate
    - Si aprendemos a usar el enumerador, YA NO NECESITAREMOS el índice para crear sumas incrementales.
    
    -Aquí le pedimos a Python, que EN VEZ de acceder DIRECTAMENTE a la LISTA, acceda a un OBJETO de tipo ENUMERATE que contenga la lista.
    Esto nos imprime UNA SERIE DE TUPLES que contiene EL INDICE (debido a numerate) y luego EL OBJETO 

lista = ["a","b","c"]

for item in enumerate(lista):
    print(item)

(0, 'a')
(1, 'b')
(2, 'c')

--------------------------------------------------------------------------------------------------------------------

- Si queremos que nos lo imprima como originalmente lo hacía, tendríamos que separar el ÍNDICE y el ITEM en el BUCLE.
- separando el ÍNDICE y el ITEM con una COMA (,) nos imprime exactamente lo mismo que el anterior ejemplo, pero de manera
    mucho más ordenada y legible que en el anterior ejemplo (sin mencionar que con su respectivo TIPO).
- Con enumerate, podemos trabajar con STRINGS, LISTAS E INTEGERS 


lista = ["a","b","c"]

for indice,item in enumerate(lista):
    print(indice,item)
    print(type(item))

--------------------------------------------------------------------------------------------------------------------------------------
'''
'''
-- EJEMPLO 3 trabajar enumerate con integers

- Por ejemplo, aquí con este rango, ENUMERATE, nos imprime de forma SECUENCIAL, del número 50 hasta el 54. También nos imprime el índice, 
    debido a que se lo indicamos (indice,item)


'''
'''

for indice,item in enumerate(range(50,55)):
    print(indice,item)
'''

'''
-- EJEMPLO 4
    - Enumerate no solamente los usamos en los loops, también lo podemos usar fuera de un loop.
    - Por ejemplo, si queremos que la siguiente lista que contiene a,b,c se TRANSFORME en una lista de tuples.
    
    -En este caso, hacemos un casting que transforme en lista el enumerate  y lo tuplice (si no nos dará error de OBJETO), 
    luego lo guardamos en una variable QUE PODAMOS IMPRIMIR.
    
    El resultado es que la lista a,b,c se CONVIRTIÓ en una LISTA que CONTIENE 3 TUPLES. (comentario marcado con #)
    
    Para DESEMPACARLOS (acceder a los tuples), lo hacemos mediante el INDICE.
    
    EN CONCLUSIÓN, cuando queramos tener ACCESSO a los ÍNDICES de un objeto ITERABLE, debemos considerar a enumerate ya que es simple.
    
'''
'''
lista = ["a","b","c"]

mis_tuples = list(enumerate(lista))
#print(mis_tuples)
print(mis_tuples[1][2])
'''

'''
-- Práctica 1 enumerador

Práctica Enumerador 1

Imprime en pantalla frases como la siguiente:

'{nombre} se encuentra en el índice {indice}'

Donde nombre debe ser cada uno de los nombres de la lista a continuación, y el índice, obtenido mediante enumerate().

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

Puedes modificar la línea print() otorgada como ejemplo, pero las frases entregadas deberán ser iguales.

Tip: utiliza loops!

'''
'''
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice,nombre in list(enumerate(lista_nombres)):
    print(f'{nombre} se encuentra en el índice {indice}')
'''
'''
suma_de_cuadrados = 0

for item,numero in enumerate(range(1,21)):
    cuadrados = numero ** 2
    suma_de_cuadrados += cuadrados
print(suma_de_cuadrados)
'''
'''
EJERCICIO 2
lista_numeros = list(range(1,101))
suma_cubos = 0


for indice,numero in enumerate(lista_numeros):
    cubos = numero ** 3
    suma_cubos += cubos
    print(suma_cubos)
print(suma_cubos)

'''
'''
palabras = ["Estudiar", "Python", "es", "emocionante"]

for indice,palabra in enumerate(palabras):
    print(f"Palabra: {palabra}, índice: {indice}")
'''

'''
PRACTICA 2 ENUMERATE

string = "Python"
lista_indices = []

for letra in enumerate((string)):
    lista_indices.append(letra)
print(lista_indices)

'''

'''
PRACTICA 3

Práctica Enumerador 3
Imprime en pantalla únicamente los índices de aquellos nombres de la lista a continuación, que empiecen con M:

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

Puedes resolverlo de diferentes maneras, pero servirá que tengas presente todos o algunos de los siguientes elementos:

Loops

Condicionales if

El método enumerate()

Métodos de strings o indexado

'''

'''
-- PRACTICA 4 

 En este ejercicio buscamos cómo hacer para IMPRIMIR los elementos que COMIENCEN con M en una lista. De la siguiente manera quedó: 
    
 En este ejercicio USAMOS EL MARAVILLOSO método de .startswith para ENCONTRAR los NOMBRES que COMIENCEN con "M" (buscando cada elemento 
    (nombre que comience con"M"))
    
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice,nombre in enumerate(lista_nombres):
    if nombre.startswith("M"):
        print(indice)
        
'''

