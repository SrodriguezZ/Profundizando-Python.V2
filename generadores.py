#Generadores 
#Es una función especial, retorna una secuencia de valores

def generador():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5 
    yield 6
gen = generador()
print(next(gen))
#intersección con for 

'''for valores in generador():
    print(f'Yield:{valores}')
'''
## Generador con while

while True:
    print(f'Generador:{next(generador())}')
    break

## generador con un for 
resultado = (valor*valor for valor in range(4))
## Suma con el generador
import math
resultado_suma=sum(valor*valor for valor in range(4))
print(f'Valor multiplicado por si mismo:{next(resultado)}')
print(f'Valor multiplicado por si mismo:{next(resultado)}')
print(f'Valor multiplicado por si mismo:{next(resultado)}')
print(f'Valor multiplicado por si mismo:{next(resultado)}')
print(f'Valor de la suma es : {resultado_suma}')

#Utilizando lista o cualquier otro iterator
lista = ["Ing","Software","Steeven"]
generador = (valor for valor in lista)
print(next(generador))
print(next(generador))

#crear un string a partir del generador creador a partir de una lista
contador = 0
def incrementar():
    global contador
    contador += 1
    return contador
resultado = (f'{incrementar()}.{nombre}' for nombre in lista)
generador = list(resultado)
print(f'Lista generada: {generador}')
print(', '.join(generador))