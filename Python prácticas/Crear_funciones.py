'''
-- Ejemplo 1

    -Crear funciones.
    Creamos funciones con def, seguido de esto, ponemos el nombre de la función y un par de paréntesis donde luego
    podremos definir lo que sucederá si ponemos una variable u objeto dentro de los paréntesis y cómo interactuará con
    el código creado dentro de nuestra función creada.
    
    - En este ejemplo, creamos nuestra función para poder saludar personas. IMPORTANTE, todo lo que queramos que sea parte
        de nuestra función debe seguir la tabulación.
        
    - Una vez que ya tengamos definida nuestra nueva y propia función, la invocamos para poder ejecutarla. Esto nos dará como resultado
        >>"Hola"
'''

# def saludar_persona():
    
   # Esta función sirve para saludar a las personas.
    
#     print("Hola")
    
# saludar_persona()

'''
-   Ejemplo 2
    - Con esta misma función, usamos los paréntesis para ahora agregar una variable (esta puede estar definida o no) para que se concatene con
        el "Hola " con la string o variable que definamos después...
        
        

'''
'''
def saludar_persona(nombre1):
    
    #Esta función sirve para saludar a las personas.
    
    print("Hola " + nombre1)
    
saludar_persona("marco")

'''

'''
-   Práctica 3 crear funciones.
Declara una función llamada cuadrado, que tome como argumento un número cualquiera, y que cada vez que sea llamada, imprima en pantalla el cuadrado de dicho número (es decir, la potencia 2 del valor).

El nombre del argumento que debe tomar dicha función es un_numero. Crea dicha variable y asígnale un número cualquiera.

Solo debes definir la función y crear la variable, no debes invocar la función luego.

'''
un_numero = 5

def cuadrado(un_numero):
    '''
    Esta función sirve para imprimir el cuadrado de un número
    '''
    print(un_numero ** 2)
