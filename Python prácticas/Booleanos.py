#EJEMPLO 1 Type de booleano y Mayúscula.
#Imprimir el type de un booleano nos arrola <class 'bool'>
#Siempre tenemos qué poner en MAYÚSCULA la primera letra de True o False, de lo
#contrario, nos arrojará un error: NameError: name 'true' is not defined. Did you mean: 'True'?
#Lo que significa que es lo mismo que hubiéramos puesto como valor un string, pero SIN las comillas.
#var1 = true 
#var2 = False
#print(type(var1))
#print(var1)
#-----------------------------------------------------------------------------------------------------
#EJEMPLO 2 Escribir un booleano INDIRECTAMENTE.
# Podemos escribir booleanos mediante operadores de COMPARACIÓN, igual que en el siguiente ejemplo.
#Esto nos da: 
#<class 'bool'>

#False
#Esto es gracias a que Python encuentra esta comparación como FALSA.
#numero = 5 > 2+3
#print(type(numero))
#print(numero)
#>>><class 'bool'>
#>>>False


#DEJAMOS AQUÍ TODOS LOS SIGNOS DE COMPARACIÓN
# == IGUAL QUE
# != DIFERENTE DE
# < MENOR QUE
# > MAYOR QUE
# <= MENOR O IGUAL QUE
# >= MAYOR O QUE
#------------------------------------------------------------------------------------------------------
#EJEMPLO 3 CREAR FUNCIÓN bool()
#ESTO ES EXACTAMENTE LO MISMO QUE EL EJEMPLO ANTERIOR.
#Podemos ser más directos y explícitos para crear boleanos con la función bool()
#Aquí preguntamos si 5 es mayor que 6, lo cuál nos da False.
#SI DEJAMOS EL PARÉNTESIS DE bool() OBTENDREMOS UN VALOR DE FALSO.

#numero = bool(5>6)
#print(type(numero))
#print(numero)
#>>><class 'bool'>
#>>>False
#------------------------------------------------------------------------------------------
#EJEMPLO 4 Booleanos a través de CONSULTAS
#Aquí consultamos a Python por medio de la variable control, si 5 ESTÁ en la variable lista.
#Por lo que nos dará TRUE O FALSE. En este caso, nos dará False, ya que 5 no se encuentra en
#la lista. Al imprimir el tipo de control, nos dice que es un bool y que control es igual a False.
#RESULTADO: 
#<class 'bool'>
#False

#lista = [1,2,3,4]
#control = 5 in lista
#print(type(control))
#print(control)
#>>><class 'bool'>
#>>>False
#-----------------------------------------------------------------------------------------------------
#De igual forma, si en el anterior ejemplo hubiéramos preguntado si 5 NO está EN la lista, nos daría
#Un bool con valor de True
#lista = [1,2,3,4]
#control = 5 not in lista
#print(type(control))
#print(control)
#>>><class 'bool'>
#>>>True