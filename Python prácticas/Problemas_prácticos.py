'''
-- Práctica 1

    Nos piden crear una función que tome como argumentos NÚMEROS DEFINIDOS, luego nos piden que:
    1.- Si la suma de estos argumentos es MAYOR a 15, devuelva el valor máximo de entre los argumentos
    2.- Si la suma es MENOR a 10, devuelva el valor mínimo de entre los argumentos
    3.- Creamos un else que por como consecuencia de que NO SE CUMPLAN las otras DOS ANTERIORES CONDICIONES:
    si suma está entre 10 y 15, devolver el número de valor intermedio (media). 
        - Para esto, importamos statistics, el cuál tiene un método para calcular la media. 
        - Después, invocamos median y nuestra lista de números la cuál almacenamos en una variable llamada intermedios

def devolver_distintos(num1,num2,num3):
    numeros = [num1,num2,num3]
    suma = num1 + num2 + num3
    import statistics
    intermedios = statistics.median(numeros)
    
    if suma > 15:
        print(max(numeros))
        return max(numeros)
    elif suma < 10:
        print(min(numeros))
        return min(numeros)
    else:
        print(intermedios)
        return intermedios
    
devolver_distintos(5,3,6)


---------------------------------------------------------------------------------

'''

'''

--  Método 2 (profesor...)

    1.- Hacemos todo lo del principio tal como lo habíamos estado haciendo, pero luego del segundo
        elif...
    2.- Luego del segundo elif, creamos un else que primero ordene numeros y luego que DEVUELVA el índice 1
        ESTO SOLO SERVIRÁ ya que nuestra función SOLO ACEPTA 3 VALORES el valor que está en el medio es el índice 1 (la mediana).
    3.- Por lo que si tuviéramos que aceptar más números, lo ideal hubiera sido usar el método que habíamos creado.
    
        NOTE pudimos haber mejorado el tercer elif cambiándolo por un else.
        
        NOTE esta función sirve aunque pongamos DESORDENADOS los valores de los números, (por ejemplo, 6,3,9) ya que .sort() los ordenaría
        y el índice 1 de la lista ordenada correspondería exactamente a la 


def devolver_distintos(num1,num2,num3):
    numeros = [num1,num2,num3]
    suma = num1 + num2 + num3
    
    if suma > 15:
        return max(numeros)
    elif suma < 10:
        return min(numeros)
    else:
        numeros.sort()
        return numeros[1]
        
print(devolver_distintos(20,5,7))

'''




'''
--  Práctica 2

    - Para este ejercicio nos piden crear una función que tome como argumento una palabra y que la devuelva
        SIN CARÁCTERES repetidos y además, ordenada alfabéticamente
        Para esto:
        1.- Definimos una función llamada ordenar que toma como argumento una palabra
        2.- Declaramos una variable llamada lista que almacena una lista vacía.
        3.- Creamos un bucle donde itere por cada letra de la palabra ingresada
        4.- Condicional de si letra NO ESTÁ en la lista vacía...
        5.- Agregamos cada letra de la palabra ingresada en nuestra lista vacía. Como tenemos la condición de que si NO ESTÁ en la lista, las letras NO se repetirán.
        6.- Dentro del append, usamos el MÉTODO lower, el cuál transformará las letras de la lista en minúsculas. Esto porque el método .sort() es SUCEPTIBLE a mayúsculas y a minúsculas.
        7.- Ordenamos alfabéticamente la palabra con la función .sort()
        8.- Imprimimos lista y devolvemos lista...

def ordernar(palabra):
    lista = []
    for letra in palabra:
        if letra not in lista:
            lista.append(letra.lower()) #aquí agregamos el método lower, para que sort pueda trabajar (ya que sort DISTINGUE entre mayús y minús)
    lista.sort()  
    print(lista)
    return lista
        
ordernar("David")

------------------------------------------------------------

--  Método del maestro (con set)

    1.- Luego de definir la función, creamos una variable llamada mi_set yla dejamos VACÍA 
    2.- Nos aseguramos de almacenar en la variable mi_set UN SET VACÍO. Esto lo hacemos mediante un typecasting y paréntesis VACÍOS set()
        - Esto ya que set NO ADMITE carácteres repetidos
    3.- Creamos un bucle por cada letra en palabra
    4.- Alimentamos a nuestro set con cada iteración del bucle mediante el método add.
    5.- Ahora tenemos un problema, los sets no son conjuntos ordenados, por lo que hacemos typecasting transformándolo en una lista.
        - Esto lo hacemos ALMACENANDO en una variable el casteo a tipo lista de mi_set
    6.- ORDENAMOS la variable mi_lista con el método .sort()
    7.- DEVOLVEMOS la variable mi_lista
    
    Este método es mejor, ya que devuelve incluso las mayúsculas de las palabras ORDENADAS. 

def ordenar(palabra):
    
    mi_set = set()
    
    for letra in palabra:
        mi_set.add(letra)
        mi_lista = list(mi_set)
        mi_lista.sort()
    return mi_lista

print(ordenar("Genaro"))

'''

'''
--  Práctica 3

    - Este ejercicio no pudimos resolverlo, pero lo haremos con la ayuda del maestro.
    1.- Necesitamos inicialmente UN CONTADOR que comience con 0, el cuál aumentará de en uno en uno y nos ayudará a definir a través de este número, cuál es
        es el índice que estamos revisando.
    2.- Creamos un bucle que pase por cada elemento de args
    3.- Control de flujo donde si args[contador] args en el índicce de contador (que al comienzo va a ser cero) es igual a 0
    4.- Esto no será suficiente, por lo que agregamos and para que SE CUMPLAN DOS CONDICIONES AL MISMO TIEMPO, las cuáles serán 
        Si args en su índice de contador (que irá a la par del índice) es igual a 0 Y EL SIGUIENTE DE ESE (args[contador + 1]) TAMBIÉN ES 0, DEVUELVA TRUE (return True).
    5.- Si no se cumple (else), hacemos que NUESTRO CONTADOR AUMENTE 1 en CADA ITERACIÓN.
        - Esto hará que VERIFIQUE CADA UNO de los elementos otorgados con la iteración del bucle for.
    6.- Hacemos también que devuelva False PERO FUERA DEL BUCLE. Esto lo hacemos poniéndolo al mismo ancho que el bucle.
        -Esto ya que recordemos que return CORTA a los bucles. Por lo que si el bucle NO ENCUENTRA la condición EN NINGUNA de las iteraciones, entonces ANTES DE QUE SALGA
        DEL BUCLE, return imprimirá False, ya que NUNCA SE CUMPLIÓ la condición. 
    7.- La última condición que nos falta cumplir es que si tenemos DOS CEROS pero en diferente lugar de la secuencia 1,0,2,3,0 NOS DARÁ ERROR, debido a que 
        La condición del bloque de control de flujo no PUDO SER VERIFICADA por la función, debido a que YA NO HAY NÚMEROS POSTERIORES, ya que HEMOS PUESTO UN 0 AL FINAL 
    8.- Para resolver esto, agregamos OTRA CONDICIÓN IF arriba de nuestro control de flujo, la cuál verificará que si:
        contador + 1 (ya que ) es IGUAL a len(args) al LARGO de nuestros argumentos ingresados, directamente imprima False.
    9.- El otro if que está debajo del nuevo if, lo convertimos en un elif, porque SI NO SE CUMPLE esa condición, probará con la siguiente (elif).
        def ceros_vecinos(*args):
    
def ceros_vecinos(*args):
    
    contador = 0
    
    for n in args:
        if contador + 1 == len(args): #Si el 0 está EN EL ÚLTIMO ÍNDICE de la secuencia de números...
            return False #Devuelva directamente el False
        elif args[contador] == 0 and args[contador + 1] == 0: #esto si los 0's repetidos están AL PRINCIPIO de la secuencia
            return True
        else: #De otra forma, que siga avanzando para verificar los demás números
            contador += 1
    return False
        
print(ceros_vecinos(1,0,2,3,0))

----------------------------------------------------------------------------------------- 
print(consecutivos_duplicados(3,4,5,3))
    #Esta función encuentra si hay NÚMEROS DUPLICADOS, no importa cuántos sean ni en qué orden estén.

def repetidos(*args):
    for n in range(len(args)):
        for i in range(n + 1, len(args)):
            if args[n] == args[i]:
                return True
    else:
        return False

print(repetidos(1,2,10,8,4,5,10))

'''

'''
--  Esta función devolverá los números pares e impares de una secuencia de números y ddevuelve un tuple.
    Primera forma (mi forma)

def contar_pares_impares(*args):
    c_pares = list()
    c_impares = list()
    
    for numero in args:
        if numero % 2 == 0:
            c_pares.append(numero)
        elif numero % 2 == 1:
            c_impares.append(numero)
        fusion = c_pares + c_impares
    return f"Numeros {tuple(fusion)}"

print(contar_pares_impares(1,2,3,4,5,6,7))

    Segunda forma (chat gpt)
    
    def contar_pares_impares(*args):
    c_pares = 0
    c_impares = 0
    
    for numero in args:
        if numero % 2 == 0:
            c_pares += 1
        elif numero % 2 == 1:
            c_impares += 1
            
    return c_pares, c_impares

# Ejemplo de uso
print(resultado = contar_pares_impares(1, 2, 3, 4, 5, 6, 7))


'''     

             

'''
--  Práctica 4 

    - Esta práctica tampoco la hicimos solos...
    - Nos piden crear una función que tome como argumento un solo número y luego que devuelva los números primos 
        desde el 0 HASTA EL RANGO MÁXIMO que será definido por el argumento otorgado Y LUEGO
        DEVOLVER LA CANTIDAD DE NÚMEROS PRIMOS que hubo.
        
    1.- Para esto primero creamos una variable llamada primos, que COMIENZA con el 2, ya que el 2 es el PRIMER NÚMERO PRIMO (0 y 1 no se toman en cuenta por convención).
        Esto hará es que si el usuario ingresa un número menor a 2, Python terminará con el programa.  
    2.- Comenzamos a verificar desde el número 3 con la variable iteración 3. Por lo que si ponemos 50 por ejemplo, comenzará a verificar desde el 3
    3.- Primero haremos el código que nos saque directamente del programa si el usuario ingresó un número primo MENOR a 2.
         Lo que hacemos es que si esta codición SE CUMPLE, DEVOLVEMOS 0.
    4.- Pero si NÚMERO SÍ ES MAYOR a 2, hacemos que pase por un bucle while que pase por cada uno de los números desde el 3 HASTA EL NÚMERO ELEGIDO, donde se va a fijar si la
        iteración es menor o igual al número entonces comenzará a hacer la verificación.
        NOTE recordar que la iteración haremos que vaya aumentando, por lo que cuando LLEGUE A SER IGUAL que número (que comenzará desde 3) SALGA del loop.
    5.- Anidamos al while un loop for que POR CADA n en RANGO de 3 hasta iteración y que salte de 2 en 2 (porque los números primos NO SON PARES)
    6.- Entonces nos fijamos si esta iteración por el módulo de n es igual a 0, entonces (si devuelve 0 entonces no es primo, ya que sería divisible por otro número y los primos NO SON DIVISIBLES por otro número). 
    7.- Si esta condición detecta que en esa iteración NO HAY UN PRIMO, le pedimos que lo salte con iteracion += 2 y usamos break para salir de esta iteración y volver al bucle while para que pueda seguir VERIFICANDO los otros números.
            Esto evitará que el número que NO SEA PRIMO, no se agregue a la lista.
    8.- Para nuestro loop for agregamos un else que sea para el caso contrario de que este número NO SEA divisible, entonces significará QUE SÍ ES PRIMO por lo que
        lo agregamos con .append(iteracion)
    9.- Luego de eso, le agregamos a iteración DOS NÚMEROS MÁS para que pueda seguir iterando en los posteriores números.
    10.- Ahora sí, podemos salir del loop e imprimir TODA  la lista de primos, para que el usuario la pueda ver y
    11.- Mostramos EL LARGO de la lista (la cantidad de números primos que hay) para decirle al usuario cuántos primos hay en su número.

def contar_primos(numero):
    primos = [2]
    iteración = 3
    
    if numero < 2:
        return 0
    
    while iteración <= numero:
        for n in range(3, iteración, 2):
            if iteración % n == 0:
                iteración += 2
                break
        else:
            primos.append(iteración)
            iteración += 2
    print(primos)
    return len(primos)    


print(contar_primos(1))

'''

def lista_primos(n):
    primos = [2]
    
    if n < 2:
        primos = []
        return primos
    
    for n in range(3, n):
        if n % 2 == 1:
            primos.append(n)
    return primos
    
print(lista_primos(20))
             

            
                
                

        