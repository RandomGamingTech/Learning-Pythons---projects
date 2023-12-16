'''
Tenemos estos argumentos indefinidos **kwargs el cuál nos ayuda no solamente a poder ingresar
carácteres indefinidos; sino que también nos permite darle un nombre.
kwargs viene de keyword, por lo que podemos deducir que esta función trabaja con diccionarios.

--  Ejemplo 1

    - Para demostrar de kwargs trabaja con diccionarios, hacemos una función llamada suma que toma 
      como variable un kwargs y luego imprime su tipo.
    - Ingresamos a nuestra función x=3, y=5. z=2 los cuales si bien no están en UN DICCIONARIO ({"x":3, "y":5, "z",2})
        podemos ver que efectivamente están dentro de un diccionario. Esto porque en realidad tenemos DOS VALORES por valor separados
        por un signo de =. Pero SON PARES de nombre y valor.

def suma(**kwargs):
    print(type(kwargs))
    
suma(x=3, y=5, z=2)

'''

'''
--  Ejemplo 2
    - Ahora crearemos una función que lo que haga sea pasar por cada uno de las claves y valores que tenemos dentro de los paréntesis y que
      los podamos ver en una impresión de pantalla.

def suma(**kwargs):
    for clave,valor in kwargs.items(): #usamos el método .items para los valores DEL DICCIONARIO que nos transforma kwargs los valores y poder trabajar con el bucle.
        print(f"{clave} = {valor}")
        
    
suma(x=3, y=5, z=2)

--------------------------------------------------------------------------

--  Ahora, ¿qué pasa si queremos sumar los valores y mostrar nuestros conjuntos?

def suma(**kwargs):
    total = 0
    for clave,valor in kwargs.items(): #usamos el método .items para los valores DEL DICCIONARIO que nos transforma kwargs los valores y poder trabajar con el bucle.
        print(f"{clave} = {valor}")
        total += valor
    return total
        
        
print(suma(x=3, y=5, z=2))

'''

'''
--  Ejemplo 3 
    - Ahora veremos como mezclar una misma función que contenga tanto argumentos normales y argumentos bien definidos (num1, num2).
    O sea que pueda recibir (num1,num2,*args,**kwargs)
    
    - Ponemos primero los argumentos normales (num1,num2), luego los argumentos de tipo *args y luego los keyword arguments.
    
    - Acomodandolos de esta manera, nuestros datos pueden ser diferenciados por el sistema para que pueda hacer lo correspondiente con ellos (lo que definamos).
     
def prueba(num1, num2, *args, **kwargs):
    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")
    
    for arg in args:
        print(f"Arg = {arg}")
        
    
    for clave,valor in kwargs.items(): #usamos el método .items para los valores DEL DICCIONARIO que nos transforma kwargs los valores y poder trabajar con el bucle.
        print(f"{clave} = {valor}")
        
    
        
        
prueba(15,50,100,200,300,400,x="uno",y="dos",z="tres")     
     
'''

'''
-- Ejemplo 4
    - También podemos aprovechar los args y los kwargs para DESEMPACAR TUPLAS o LISTAS o DICCIONARIOS.
    
    - Aquí hacemos exactamente lo mismo, solamente que PASAMOS los *args a una variable con el mismo nombre e
        hicimos los mismo con los **kwards
    - De esta manera, estamos desempacando UNO A UNO la secuencia de números y el diccionario. 

def prueba(num1, num2, *args, **kwargs):
    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")
    
    for arg in args:
        print(f"Arg = {arg}")
        
    
    for clave,valor in kwargs.items(): #usamos el método .items para los valores DEL DICCIONARIO que nos transforma kwargs los valores y poder trabajar con el bucle.
        print(f"{clave} = {valor}")
        
    
args = 100,200,300,400

kwards = {"x":"uno","y":"dos","z":"tres"}
        
prueba(15,50,*args,**kwards)  

'''


'''
-- Práctica 1 kwargs
    - Nos piden crear una función que cuente la cantidad de parámentros que se entreguen y devuelva esa cantidad como resultado.
    
def cantidad_atributos(**kwargs):
    resultado = 0
    for clave,numero in kwargs.items():
        resultado += 1
    print(resultado)
    return resultado
    
cantidad_atributos(x=1,y=2,z=3)
    
'''

'''
--  Práctica 2
    Nos piden crear una función que devuelva en forma de lista los valores ingresados con una clave (en otras palabras, los valores de un diccionario).

def lista_atributos(**kwargs):
    lista = []
    for clave,valor in kwargs.items():
        lista.append(valor)
    return lista


cosas = {"x":1,"y":2,"z":3}

print(lista_atributos(**cosas))

'''

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave,valor in kwargs.items():
        print(f"{clave}: {valor}")
    
           
