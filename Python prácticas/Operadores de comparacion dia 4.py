#EJEMPLO 1 SIGNO == (igualdad)
#Este signo "=" (igual) es para ASIGNARLE un VALOR a ALGO.

#El signo "==" es para ver si un valor es IGUAL a OTRO.
#mi_bool = 10==25
#print(mi_bool)
#>>>False

#También podemos comparar OPERACIONES que den como RESULTADO un NÚMERO
#Y comparar si este son iguales.
#mi_bool = 5+5==18-8
#>>>True

#También podemos comparar STRINGS, TENER EN CUENTA que las strings son SENSIBLES
# A las MAYÚSCULAS.
# Hacemos una COMPARACIÓN de STRINGS en el siguiente ejemplo:
#mi_bool = "blanco" == "negro"
#print(mi_bool)
#>>>False

#Como las strings son SENSIBLES a las MAYÚSCULAS, una forma de hacerlas equivalentes
#es mediante el método .lower() el cuál al transformar las letras a minúsculas, el resultado 
#Este ejemplo nos dará True, aunque ORIGINALMENTE la N estuviera en Mayúsculas
#mi_bool = "blanco" == "Blanco".lower()
#print(mi_bool)
#>>>True

#También podemos comparar valores de DISTINTOS TIPOS 
#mi_bool = "100" == 100
#print(mi_bool)
#>>>False

#Al comparar INTEGERS con FLOATS, si estos tienen el MISMO VALOR, entonces
#AUNQUE sean DIFERENTES, dará True, como en el siguiente ejemplo:
#mi_bool = 100 == 100.00
#print(mi_bool)
#>>>True
#---------------------------------------------------------------
#Ejemplo 2 SIGNO != (Diferencia)
#Esto nos indica si UN VALOR es DIFERENTE a OTRO
#El resultado de esto nos da False, debido a que los comparadores PUEDEN
#Comparar Floats con Integers y COMPARA si su VALOR es EQUIVALENTE.
#mi_bool = 100 != 100.00
#print(mi_bool)
#>>>False
#---------------------------------------------------------------
#Ejemplo 3 >= y <= (Mayor o igual o Menor o igual que)
#Este ejemplo nos da True debido a que 5 es mayor o IGUAL a 5-
#mi_bool = 5 >= 5
#print(mi_bool)
#--------------------------------------------------------------------------------
#Ejemplo 4 MÁS DE DOS COMPARACIONES Para esto necesitamos OPERADORES LÓGICOS
#Los cuáles veremos en la próxima clase.



