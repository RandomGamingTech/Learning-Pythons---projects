#Python nos permite seleccionar un FRAGMENTO del texto de la string. Para eso
#nos permite DESDE dónde seleccionar (con el primer número) HASTA dónde (segundo número)
#dentro de los corchetes.
#NOTA el último caracter del límite del rango, NO SE SELECCIONARÁ, en este caso, 
#[2:5] nos da de la C a la E (CDE)
#texto = "ABCDEFGHIJKLM"
#fragmento = texto[2:5]
#print(fragmento)
#-------------------------------------------------------------------------------------
#EJEMPLO 2
#Si solamente dejamos [2:] Python interpretará que queremos seleccionar desde el 2, 
# hasta el final de la cadena.
#este ejemplo da como resultado CDEFGHIJKLM
#texto = "ABCDEFGHIJKLM"
#fragmento = texto[2:]
#print(fragmento)
#-----------------------------------------------------------------------------
#EJEMPLO 3
#Si lo hacemos al revés, o sea [:5] Python interpretará esto como desde 
#donde COMIENZA 0 HASTA el 5.
#El resultado de esto es: ABCDE
#texto = "ABCDEFGHIJKLM"
#fragmento = texto[:5]
#print(fragmento)
#--------------------------------------------------------------------------
#Ejemplo 4
#Si agregamos un TECER FACTOR le indicaremos a Python CADA CUÁNTOS caracteres
#tiene que ir extrayendo.
#el resultado de esto es CEGI debido a que Python comenzó a a contar desde
#el primer número establecido en la búsqueda (2) luego de eso, cada 2 carácteres contaba, 
#hasta llegar al límite del rango establecido (o sea, 10)
#RECORDAR, QUE SI EL SIGUIENTE CONJUNTO SE ENCUENTRA EN EL LÍMITE DEL RANGO
#ESTABLECIDO EN EL SEGUNDO CARACTER DE LA EXTRACCIÓN (EL 10) TAMPOCO LO 
#TOMARÁ EN CUENTA DEBIDO A QUE ESTÁ EN EL RANGO LÍMITE.
#texto = "ABCDEFGHIJKLM"
#fragmento = texto[2:10:2]
#print(fragmento)
#---------------------------------------------------------------------------
#EJEMPLO 5
#luego tenemos el mismo caso, pero extrayendo CADA 3, aquí en este ejemplo, 
#vemos que COMENZARÁ desde la C a contar, DEBIDO a que es lo que ESTABLECIMOS
#en el primer término de la búsqueda (2) y de ahí, extrajo cada 3 caracteres:
#El resultado de esto es: CFI
#texto = "ABCDEFGHIJKLM"
#fragmento = texto[2:10:3]
#print(fragmento)
#-------------------------------------------------------------------------
#EJEMPLO 6
#Si dejamos vaciós el PRIMER Y SEGUNDO término de la búqueda, Python
#arrojará el TÉRMINO 0 y luego de ahí, comenzará a contar cada tercer término
#Como NO tenemos un rango límite, contará CADA 3 hasta el FINAL de la cadena
#el resutado de este ejercicio es: ADGJM
#texto = "ABCDEFGHIJKLM"
#fragmento = texto[::3]
#print(fragmento)
#-------------------------------------------------------------------------
#EJEMPLO 7
#Ahora, igual que en el ANTERIOR ejemplo, dejamos vacíos los DOS primeros factores
#y solo dejamos el TERCERO, pero esta vez NEGATIVO, por lo que Python 
#Comenzará a contar DESDE 0, PERO, INVERSAMENTE, O SEA, LA M SERÁ el ELEMENTO 0
#De ahí en adelante, contará CADA 3, durante TODA LA CADENA.
#El resultado de este ejercicio es: MJGDA
#texto = "ABCDEFGHIJKLM"
#fragmento = texto[::-3]
#print(fragmento)
#-----------------------------------------------------------------------------
#EJEMPLO 8 
#Este ejemplo es de la misma naturaleza que el anterior, solamente que en vez de 
#contar cada -3, SI CONTAMOS CADA -1, Python INVERTIRÁ la cadena, por ejemplo:
#frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
#print(frase[::-1])
#El resultado de este ejercicio es: azevrec ut nebeb es on y odot nadreucer ol ,netucsid oN .serodanedro noc rajabart laineg sE 





