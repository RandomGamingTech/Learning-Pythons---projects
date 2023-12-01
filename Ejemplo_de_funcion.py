'''
--  PRIMER EJEMPLO
    - Vamos a hacer una FUNCIÓN que nos ayude a DESEMPACAR TUPLES.
    
    - Primero vamos a realizar un EJEMPLO de cómo DESEMPACAR TUPLES.
    
    1.- Hacemos una variable que CONTIENE una LISTA de TUPLES
    2.- Creamos un loop for que pase por cada elemento y sub-elemento en la lista (como es una lista de tuples, podemos poner que pase por ambos valores, en este caso, cafe y precio)
    3.- Por cada iteración, imprimimos cafe
    
    - NOTE incluso pudimos haber impreso un cierto % del costo del café, imprimiendo precio % x 

precios_cafe = [("capuchino",1.5),("Expresso",1.2),("Moka",1.9)]

for cafe,precio in precios_cafe:
    print(cafe)

'''

'''
--  El anterior ejemplo nos servía bien, pero ¿qué tal si hubiésemos querdo averiguar cuál café es el más costoso?
        entonces ahí hubieran venido como anillo al dedo las funciones ya que podemos crear una función
        que pase por cada uno de los elementos y que VAYA RETENIENDO, aquel que tiene el precio mayor.
        
        1.- Agregamos nuestra lista de precios_cafe
        2.- Definimos el nombre de la definición y ponemos como argumento la lista_precios (que será nuestra variable precios_cafe)
        3.- Declaramos una variable antes del bucle llamada precio_mayor, donde se actualizará por cada nuevo valor que sea mayor a la misma.
        4.- Declaramos otra variable llamada cafe_caro donde declaramos una string vacía, la cuál será llenada por el nombre del café más caro (el otro elemento del tuple con el valor más alto)        
        5.- Hacemos un loop for donde pedimos ambos elementos del tuple de nuestra lista de tuples que contienen el nombre y el precio de cada cafe
        6.- Ponemos una condición if donde si precio es MAYOR a precio_mayor (que tiene valor INICIAL de 0)
        7.- La variable precio_mayor (0) pasará a ser IGUAL al valor de precio 
        8.- Por último, la variable cafe_caro (con valor inicial de string vacio) pasará a ser la string del tuple con mayor valor.
        9.- Agregamos un return, donde nos devuelva el cafe_caro y el precio_mayor
        10.- Hacemos una variable que almacena la lista precios_cafe TRATADA por nuestra función
        11.- imprimimos la variable cafe_mas_caro
        
precios_cafe = [("capuchino",1.5),("Expresso",200),("Moka",1.9)]

def cafe_caro(lista_precios):
    precio_mayor = 0
    cafe_caro = ""
    for cafe,precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_caro = cafe
    
    return (cafe_caro, precio_mayor)

cafe_mas_caro = cafe_caro(precios_cafe)

print(cafe_mas_caro)

>>('Expresso', 200)

----------------------------------------------------------------------------------

--  Adicionalmente. También podemos hacer una DESCOMPRESIÓN EXTRA de tuples para obtener    
    solamente el nombre del cafe y la variable valor por separado (sin que nos devuelva el tuple).
    
    - Esto lo hacemos creando el nombre de DOS VARIABLES, SEPARADAS POR UNA COMA (,) esto lo que hará
        es dividir ambos valores en 2 (los valores que contiene el tuple, nombre y precio) para asignarselos 
        a las variables cafe y precio.
        
>>Expresso 200    

precios_cafe = [("capuchino",1.5),("Expresso",200),("Moka",1.9)]

def cafe_caro(lista_precios):
    precio_mayor = 0
    cafe_caro = ""
    for cafe,precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_caro = cafe
    
    return (cafe_caro, precio_mayor)

cafe,precio = cafe_caro(precios_cafe)
print(cafe,precio)

'''     








