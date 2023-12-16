'''
--  Ejemplo 1
    - Actualmente, solamente creamos funciones las cuales pueden tomar un número determinado como argumento...
    - Esto está bien, pero tenemos el problema de que si el usuario ingresa MÁS DE DOS ARGUMENTOS (en este caso)
        Python nos devolverá un error.

def suma(a,b):
    return a+b

print(suma(5,6))

'''

'''
--  Ejemplo 2
        - Gracias a *args podemos hacer funciones con argumentos INDEFINIDOS
        - Por lo que podemos crear una definición que tome argumentos INDEFINIDOS (*args)
            luego creamos una variable con valor de 0 llamada total
            Creamos un loop for para que pase por cada arg en args y la variable total se actualice a la suma de total + el argumento actual de la iteración
            luego que devuelva total

def suma(*args):
    total = 0
    
    for arg in args:
        total += arg 
        
    return total

print(suma(1,4,5,6,8))

'''

'''
--  Ejemplo 3 el anterior ejemplo también pudimos haberlo hecho de una forma mucho más sencilla usando la función sum:

def suma(*args):
    return sum(args)

print(suma(1,4,5,6,8))

'''


'''
--  Práctica 1 argumentos indefinidos
    - Nos piden crear una función que eleve al cuadrado una secuencia de números y luego SUME toda la secuencia...

def suma_cuadrados(*args):
    suma = 0
    for numero in args:
        numero = numero ** 2
        suma += numero
    print(suma)
    return suma 
        
suma_cuadrados(2,2,2)

'''

'''
-- Práctica 2
    - En esta ocasión, nos piden crear una función que convierta los números negativos a positivos, por lo que aquí usamos
        el método abs, el cuál transforma cualquier número en absoluto
    1.- Creamos una def llamada suma_absolutos la cuál toma argumentos indefinidos
    2.- Creamos una variable llamada suma donde almacenaremos la suma de nuestros absolutos
    3.- Creamos un loop for que pasa por cada numero en args
    4.- Condicional if que transforma en ABSOLUTO un número SI ESTE ES MENOR A 0
    5.- Actualizamos la variable suma para que se sume por cada número en args (el resultado será la suma total de la secuencia de números absolutos)
    6.- Imprimimos la suma y RETORNAMOS la suma

def suma_absolutos(*args):
    suma = 0
    for numero in args:
        if numero < 0:
           numero = abs(numero)
        suma += numero
    print(suma)
    return suma

suma_absolutos(1,5,4)

'''

'''
--  Práctica 4
'''

def numeros_persona(nombre,*args):
    suma_numeros = 0
    for numero in args:
        suma_numeros += numero
    print(f"{nombre}, la suma de tus números es {suma_numeros}")
    return f"{nombre}, la suma de tus números es {suma_numeros}"
    
numeros_persona("Daniel",1,3,4)

