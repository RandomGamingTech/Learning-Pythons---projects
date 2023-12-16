'''
Ejemplo 1. 

def lanzar_dados():
    valor1 = 0
    valor2 = 0
    from random import randint
    valor1 = randint(1,6)
    valor2 = randint(1,6)
    return valor1,valor2

def evaluar_jugada(valor1,valor2):
    suma_dados = valor1 + valor2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

 
tirar1,tirar2 = lanzar_dados()

evaluar_jugada(tirar1,tirar2)

'''

'''
--  Práctica 2

    - En esta práctica, nos han pedido que crearamos dos funciones.
    -- Primera función
        - La primera toma una lista de numeros y ELIMINA sus números repetidos y ELIMINA también su número MAYOR
        - Para lograr lo PRIMERO (quitar repetidos), primero creamos una función llamada reducir_lista, la cual toma como argumento una lista
            - Luego creamos una variable INTERNA llamada lista_sin_repetidos que contiene UNA LISTA VACÍA
            - Luego, creamos un bucle for que pase por cada elemento de la lista
            - Si número NO está en lista, que se añada en lista_sin_repetidos (la lista vacía), esto por medio del método .append(numero)
            - 
        - Para elimnar su NÚMERO MAYOR
            - Creamos una variable llamada max_num la cual usa la función max() y dentro pusmos la lista_sin_repetidos
            - Posteriormente invocamos a la lista_sin_repetidos y usamos el método .remove() y dentro ponemos la variable que contiene el VALOR MÁXIMO de la lista (max_num)
                Lo INVOCAMOS debido a que NO PODEMOS ALMACENAR .remove() solo invocarlo
                Por último, agregamos un return QUE NOS DEVUELVA la lista_sin_repetidos, la cuál ya NO TIENE REPETIDOS y su VALOR MÁXIMO ha sido ELIMINADO
                
    -- Segunda función
        - Para esta función la cuál dará el promedio de los números de la lista ya transformada por la función anterior...
            - Primero creamos una función llamada promedio la cual toma como argumento una lista
            - Segundo, hacemos un return que NOS DEVUELVA la suma de la lista (con sum(lista)) ENTRE / la longitud de la lista (len(lista))
    
    Finalmente las imprimimos en un formato que nos arroja la lista transformada y el promedio.
    
    NOTE tenemos que invocar ambas funciones en orden, si no no servirá.

lista_numeros = [1,2,2,3,4,5,5,5,6,7]

def reducir_lista(lista):
    lista_sin_repetidos = []
    for numero in lista:
        if numero not in lista_sin_repetidos:
            lista_sin_repetidos.append(numero)
    max_num = max(lista_sin_repetidos)
    lista_sin_repetidos.remove(max_num)
    return lista_sin_repetidos

def promedio(lista):
    return sum(lista) / len(lista)
    
    
reducido = reducir_lista(lista_numeros)

promediar = promedio(lista_numeros)

print(f"Tu lista sin numeros repetidos es {reducido} y su promedio es de {promediar}")

def lanzar_moneda():
    moneda = ["Cara", "Cruz"]
    from random import choice
    cara_cruz = choice(moneda)
    print(cara_cruz)
    return cara_cruz
    
def probar_suerte(cara_cruz,lista):
    if "Cara" in cara_cruz:
        lista.clear() #Eliminamos los elementos de la lista con el método .clear()
        print(f"La lista se autodestruirá {lista}")
        return lista #Importante, para la prueba tenemos que devolver la lista, si no nos marcaba error
    else:
        print(f"La lista fue salvada {lista}")
        return lista #El mismo caso, tenemos que devolver aquí también la lista, si no nos marcaba error.
        
lista_numeros = [1,2,3,4,5]

probar_suerte(lanzar_moneda(),lista_numeros)

'''







