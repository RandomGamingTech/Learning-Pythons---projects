def numeros_ganadores_melate():
    from random import randint
    Numero1 = randint(1,10)
    numero2 = randint(11,20)
    numero3 = randint(21,30)
    numero4 = randint(31,40)
    numero5 = randint(41,45)
    numero6 = randint(46,56)
    return f"Primer número: {Numero1}\nSegundo número: {numero2}\nTercer número: {numero3}\nCuarto número: {numero4}\nQuinto número: {numero5}\nSexto número: {numero6}"

print(numeros_ganadores_melate())