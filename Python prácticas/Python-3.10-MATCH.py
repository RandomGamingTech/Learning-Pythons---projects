'''
-- PATRONES ESTRUCTURALES.

    - Python nos ha traído una nueva actualización, la 3.10 (la que estábamos ya usando). Esta actualización nos ha traído
    un cambio bastante importante que es las coincidencias de PATRONES ESTRUCTURALES.
    - Antes de la versión 3.10 a Python le faltaba una HERAMIENTA que está disponible EN CASI TODOS los lenguajes de programación
        la cuál es una variedad de if que nos permite ELEGIR entre una OPCIÓN entre una SERIE de OPCIONES.
    - En los otros lenguajes, esta herramienta se suele llamar switch o Switch Keys y en Python, a partir de la versión 3.10,
        la incorpora y se llama MATCH (match), que significa "coincidencia".
    - Match no solo nos va a permitir una opción entre varias, sino que además nos va a permitir implementar que nuestro código haga ALGO DISTINTO 
        de acuerdo a un patrón que estemos recibiendo.    

'''
'''
--  En el siguiente ejemplo tenemos la variable serie la cuál tiene un valor de "N-02". Creamos un bloque condicional en el cuál pedimos condiciones específicas
    por en caso que determinado valor se almacene en la variable.


serie = "N-02"

if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")
else:
    print("No existe ese producto")
    
>>Nokia

-----------------------------------------------
--  Match nos permitirá hacer esto de una manera algo distinta pero con MUCHAS OTRAS VENTAJAS.
    Aquí, ponemos si HAY UNA COINCIDENCIA con la variable serie, ENTONCES:
    En CASO de que sea "N-01" imprimir "Samsung" y así sucesivamente.   
    - AQUÍ EL EQUIVALENTE DE ELSE ES: case _:
    
    - Esto nos imprime EXACTAMENTE LO MISMO y AHORRÁNDONOS ESCRITURA.  


serie = "N-02"

match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No existe ese producto")
        
>>Nokia

'''

'''
--  Match no solamente nos ayuda a hacer lo mismo que con los bloques condicionales tradicionales de if, elif y else; sino que
    también podemos hacer cosas como la siguiente mezclándola CON LOOPS.
    
    - En el siguiente ejemplo, creamos DOS variables, que contienen 1 diccionario. 
    - Luego, MEZCLAMOS estas variables, en una NUEVA variable llamada elementos y elementos contiene además también una string llamada libros (la cuál
        en este ejemplo no es importante).
    - Entonces, hacemos un bucle que por CADA elemento (e), en elementos, BUSQUE UNA COINCIDENCIA de:
        en CASO de que HAYA un DICCIONARIO con clave "nombre":y su elemento (nombre), una clave "edad" y su elemento (edad) y otra clave "ocupacion" y su 
        elemento (ocupacion) IMPRIMA 
        1.- la string "Es un cliente"
        2.- El elemento nombre (el valor de la clave "nombre") el elemento edad ("el valor de la clave edad") y el elemento ocupacion (el valor de la clave "ocupacion").
        - Esto nos imprime como resultado >> Es un cliente
                                          >> Federico 45 instructor


cliente = {"nombre":"Federico",
           "edad":45,
           "ocupacion":"instructor"}

pelicula = {"titulo":"Matrix",
            "ficha_tecnica":{"protagonista":"Keanu reeves",
                             "director":"Lana y Lilly Wachowski"}}

elementos = [cliente, pelicula, "libro"]

for e in elementos:
    match e:
        case {"nombre": nombre,
              "edad": edad,
              "ocupacion": ocupacion,}:
            print("Es un cliente")
            print(nombre,edad,ocupacion)
            
>> Es un cliente
>> Federico 45 instructor

-------------------------------------------------------------

-   Ahora, ¿qué pasaría si hay un caso distinto compuesto por un "titulo" con un valor de titulo, luego
    una "ficha_tecnica" que sea "ficha_tecnica" y que EL VALOR de esta "ficha_tecnica" esté compuesto por un    
    diccionario {} que contenga PRIMERO una clave {"protagonista"} con un item como VALOR de protagonista {"protagonista":protagonista}
    y luego una clave de "director" con un item como valor de director {"protagonista":protagonista, "director":director}
    - Si este fuera el caso dentro de nuestro elemento de la lista elementos, entonces vamos a imprimir  la STRING "esto es una película"
        y luego el ELEMENTO titulo, protagonista y director...  
    -Luego agregamos UN CASO FINAL (equivalente de else) case _: en donde encontrará a "libro" (la string que mezclamos junto a las variables cliente)
        y pelicula) imprimirá "no se que es esto"

'''

cliente = {"nombre":"Federico",
           "edad":45,
           "ocupacion":"instructor"}

pelicula = {"titulo":"Matrix",
            "ficha_tecnica":{"protagonista":"Keanu reeves",
                             "director":"Lana y Lilly Wachowski"}}

elementos = [cliente, pelicula, "libro"]

for e in elementos:
    match e:
        case {"nombre": nombre,
              "edad": edad,
              "ocupacion": ocupacion,}:
            print("Es un cliente")
            print(nombre,edad,ocupacion)
        case {"titulo":titulo,
              "ficha_tecnica":{
                  "protagonista":protagonista,
                  "director":director}}:
            print("esto es una pelicula")
            print(f"La pelicula es: {titulo}, el protagonista es {protagonista} y los directores son {director}")
        case _:
            print("No se que es esto")
            