'''
--  EJEMPLO 1 ENFOQUE TRADICIONAL, COMPRESIÓN DE LISTAS

    - Hasta ahora hemos estado usando este enfoque para agregar elementos a una lista
        por cada iteración de un loop. Donde por cada itineración de la variable palabra,
        nos agregue su elemento (cada letra) a lista (la cuál está vacía)
  
palabra = "python"

lista = []

for letra in palabra:
    lista.append(letra)
    
print(lista)  

>>['p', 'y', 't', 'h', 'o', 'n']
        
'''

'''
--  EJEMPLO 2 COMPRESIÓN DE LISTA

    - El anterior ejemplo nos hubiera tomado MENOS LÍNEAS DE CÓDIGO, si lo hubieramos
        hecho desde otro enfoque.
        
    - Aquí lo hacemos DIRECTAMENTE en la lista. La sintaxis explicada sería la siguiente:
        "Una lista COMPUESTA de Letra por cada letra en palabra", esto va a iterar por cada LETRA en Python.
    - Esto lo que realizará es una lista en la cuál CADA ELEMENTO, va a ser UNA LETRA de CADA LETRA
        que haya en PALABRA

palabra = "python"

lista = [letra for letra in palabra]


print(lista) 

>>['p', 'y', 't', 'h', 'o', 'n']

----------------------------------------------------------------------------------------------------------------------

--  Ahora en vez de poner una variable que contenga la string "python", directamente ponemos la string en el mismo bucle...
    Esto nos imprime exactamente el mismo resultado que antes.


lista = [letra for letra in "python"]

print(lista)

>>['p', 'y', 't', 'h', 'o', 'n']

'''


'''
--  EJEMPLO 3, TRABAJAR CON VALORES NUMÉRICOS

    - Supongamos que queremos que nuestra lista esté compuesta por un número por cada número que tengamos dentro, entonces...

numeros = [numero for numero in range(1,21)]
print(numeros)

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


'''

'''
--  EJEMPLO 4, MODIFICAR NÚMEROS 
    - Por ejemplo, queremos que nuestra lista esté compuesta por CADA NÚMERO, pero DIVIDIDO ENTRE DOS, por CADA NÚMERO que haya en el siguiente
        rango...


lista = [numero / 2 for numero in range(0,21)]
print(lista)


>>[0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0]  

'''

'''
--  EJEMPLO 5, COMPRESIÓN CON IF 
    - Podríamos incluso incorporar un condicional if para ver SI ALGUNO de nuestros números los INCORPORAMOS y a OTROS NO.
    - Aquí lo que le pedimos a Python es una lista de número por cada número que esté en rango de 0 a 21 (0 a 20) SI NÚMERO ES
        MULTIPLICADO POR 2 ES MAYOR A 10.
        
    - ESTO NOS DA COMO RESULTADO AQUELLOS NÚMEROS QUE SOLAMENTE CUMPLEN CON LA CONDICIÓN ANTERIOR.

lista = [numero for numero in range(0,21) if numero * 2 > 10]
print(lista)

>>[6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

-- ¿Qué pasaría si nosotros también pusiéramos un else para tener una ALTERNATIVA, que los números no cumplan con la condición, hagan otra cosa...

    - Para eso TENDRÍAMOS QUE ESCRIBIR EL CONDICIONAL ANTES DEL BUCLE, PERO DESPUÉS DEL PRIMERO "ELEMENTO".
    
    -- Aquí le decimos a Python que queremos una lista de numero SI numero * 2 es MAYOR a 10 por CADA NÚMERO en un rango de 0,21, 
        de otra forma, que imprima la palabra "no" 


lista = [numero if numero * 2 > 10 else "no" for numero in range(0,21)]
print(lista)

>>['no', 'no', 'no', 'no', 'no', 'no', 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

'''

'''
--  NOTE, A MAYOR EFICIENCIA, MENOR LEGIBILIDAD.
'''

'''
--  EJEMPLO 6 

    - Ahora veremos un ejemplo de la vida real. Supongamos que tenemos una lista de medidas en pies.
    - Aquí lo que queremos es que nos de OTRA LISTA pero que esté TRANSFORMADA a METROS. 
        Para esto hay que DIVIDIRLO entre 3.281.

pies = [10,20,30,40,50]
metros = [numero * 3.281 for numero in pies]
print(metros)

'''

'''
-- PRACTICAS COMPRESION DE LISTAS

    -Aquí nos pedían una LISTA llamada valores_cuadrado donde se almacenen los CUADRADOS de la lista llamada VALORES.
    
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [numero ** 2 for numero in valores]
print(valores_cuadrado)
    
'''
temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [grado -32 for grado in temperatura_fahrenheit if grado *5/9 >= 0]
print(grados_celsius)