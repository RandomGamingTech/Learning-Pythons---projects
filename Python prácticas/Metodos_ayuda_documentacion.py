'''
    -- Los métodos de los objetos son muchísimos, por los que nos tardaríamos toda una vidas en aprenderlos y memorizarlos
        todos. En su lugar podemos utilizar la función ayuda o la documentación de Python.
        
    -- Este método (pop) nos elimina el último item del diccionario.
'''


'''
Práctica 1.- Nos piden investigar en la documentación, pero francamente, creo que chat gpt es mucho mejor instructor.

-- Descubrimos que lstrip es un método que nos permite ELIMINAR los valores de la IZQUIERDA (lstrip, l de left) que le
    especifiquemos poniéndolos entre comillas DENTRO de los paréntesis del método.
    -Si quisieramos eliminar DETERMINADOS elementos de la DERECHA, usaríamos .rstrip() (r de right)
    - Si quisiéramos eliminar carácteres específicos del elemento en general, usaríamos solamente .strip()


a = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

print(a.lstrip(",:%_#"))

>>Pyt%on_ _Total,,,,,,::#

'''

'''
-- Práctica 2.
    -Nos piden buscar en la documentación de Python acerca del método insert() para poder
        añadir el elemento "naranja" como CUARTO elemento de la lista frutas.
    - Buscamos en chat gpt y nos arrojó que insert() toma dos argumentos. El primero, es el índice
        en donde queremos instertar nuestro objeto.
    - Esto lo que hace es INSERTAR el objeto deseado y DESPLAZAR el siguiente un lugar POSTERIOR en el índice.
        El segundo argumento que toma es el del objeto que queremos insertar.
    - NOTE este método NO DEVUELVE nada, por lo que hay que invocarlo PRIMERO.


frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3,"naranja")
print(frutas)

>>['mango', 'banana', 'cereza', 'naranja', 'ciruela', 'pomelo']

'''

'''
--  Práctica 3
    - Nos piden verificar si los siguientes sets, forman CONJUNTOS AISLADOS (o sea, que no tienen elementos en común)
        usando el método isdisjoint()
    - Luego, que almacenemos los resultados en una variable llamada conjuntos aislados.
    - El método .isdisjoint toma como valor la VARIABLE que queremos comparar SI NO TIENE elementos en común.
        Si no tiene, devolverá True, pero si sí tiene elementos repetidos, dará False.
    - En este caso, nos devuelve False (ya que sí tiene elementos repetidos, entonces NO es un conjunto AISLADO).


marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)

print(conjuntos_aislados)


>>False
'''

