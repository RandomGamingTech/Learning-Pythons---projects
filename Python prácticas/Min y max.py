'''
-- EJEMPLO 1 MENOR con NÚMEROS. (FORMA 1)
    - En este ejemplo, hemos creado una serie de números almacenados en una variable llamada menor. Luego,
    usamos la función menor para EXTRAER el NÚMERO MENOR.
    - Esto nos imprime 35, debido a que es el número MENOR de la secuencia.
    
menor = min(58,96,72,64,35)
print(menor)

>>35

-------------------------------------------------------------------------------------------------------------------------

-- MÁXIMO CON NÚMEROS: (FORMA 2)

    - Si nosotros quisiéramos buscar el número MAYOR de una secuencia de números, en lugar de escribir la función min, escribiríamos
    max.
    Esto nos dará el número mayor de la secuencia de números.

mayor = max(58,96,72,64,35)
print(mayor)

>> 96

'''
'''
-- EJEMPLO 2 FORMA 2 para MIN Y MAX
    -También podríamos hacerlo de otra forma, como en el siguiente ejemplo.
    - Podemos trabajar estas funciones con LISTAS. 
        Aquí creamos una lista, y después imprimimos el MÁXIMO de los números en LISTA
    
lista = [58,96,72,64,35]

print(max(lista))

----------------------------------------------------------------------------------------------------------------

    - También podríamos crear una cadena donde pongamos una frase donde expresemos el mínimo y el máximo de una lista, como
        en el siguiente ejemplo:

lista = [58,96,72,64,35]

print(f"El menor es {min(lista)} y el mayor es {max(lista)}")

'''

'''
-- NOTE recordar que dentro de min y max podemos poner una variable que tenga una COLECCIÓN como una lista, un diccionario o un tuple o 
    una serie de números.

'''

'''
--  EJEMPLO 3 min y máx con STRINGS

    - min y max también pueden trabajar ALFABÉTICAMENTE.
    En la lista nombres, tenemos una serie de nombres y queremos saber QUIÉN tiene el PRIMER LUGAR en ORDEN ALFABÉTICO.
    - Como alicia comienza con A y la A es la MENOR ALFABÉTICAMENTE, nos imprime alicia. 
    
nombres = ["juan", "pablo", "alicia", "carlos"]
print(min(nombres))

>>alicia

-------------------------------------------------------------------------------------------------------------------------

-   Ahora, ¿qué pasaría si solamente tuviéramos una sola string almacenada en una variable?
    - En este caso, nos imprimirá C... ¿por qué?, pues porque PRIMERO busca en las letras MAYÚSCULAS y luego en las MINÚSCULAS.

nombre = "Carlos"

print(min(nombre))

>>C

------------------------------------------------------------------------------------------------------------------------------------

    - Si quisiéramos que ese error NO sucediera, entonces lo que tendríamos que hacer es usar el MÉTODO LOWER para transformar todas a MINÚSCULAS
        y ahora sí, buscar el mínimo o el máximo. Esto nos dará a, porque es la menor alfabéticamente.
        
nombre = "Carlos"

print(min(nombre.lower()))

>>a        

'''

'''
    -- EJEMPLO 4 min y max con diccionarios. 
        - Aquí tenemos un ejemplo donde hay un diccionario, donde la clave ALFABÉTICAMENTE más PEQUEÑA es la C1 que C2, pero su VALOR MÁS BAJO es el de la 
            clave C2 (11).
        - Esto nos imprime C1, porque se ha fijado POR DEFECTO en la CLAVE que tiene el valor más PEQUEÑO (alfabéticamente).

dic = {"C1":45, "C2":11}
print(min(dic))

>>C1

----------------------------------------------------------------------------------------------------------------------------------------------------------------

    - Si ahora quisiéramos que nos devolviera EL VALOR más pequeño, entonces lo tendríamos qué hacer con el MÉTODO .values el cuál se fija EN EL VALOR de la CLAVE.
        - Esto ahora sí nos arrojará el VALOR más BAJO

dic = {"C1":45, "C2":11}
print(min(dic.values()))

>>11

'''

'''
    -- PRÁCTICA 3 min y max 


'''
diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

edad_minima = min(diccionario_edades.values())

ultimo_nombre = max(diccionario_edades)

print(f"La edad mínima es de {edad_minima} y el último nombre es {ultimo_nombre}")





