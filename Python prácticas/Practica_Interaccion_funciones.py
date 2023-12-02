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

