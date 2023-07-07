rango = range(11)
lista =[] 
#Imprime los valores divisible de 2, con sentencia for y if 
lista = [numero for numero in rango if numero%2==2]
#print(f'Lista comprimida: {lista}')
# imprime dos sentencia if y un for, separando numeros divisible de 2 y impares
lista_pares = []
lista_impares = []
[lista_pares.append(numero) if numero%2==0 else lista_impares.append(numero) for numero in range (11)]
print(f'Numeros pares:{lista_pares}')
print(f'Numeros impares:{lista_impares}')
#suma de numeros pares en lista
import math 
print(F'Suma de par:{sum(lista_pares)}')
#separa una lista de lista a una lista
lista_lista = [[1,2,3],[4,5,6],[7,8,9,10]]
lista_nueva = [valor for sublista in lista_lista for valor in sublista]
lista_pares_ = [valor+valor for sublista in lista_lista for valor in sublista if valor%2==0]
print(F'Nueva Lista:{lista_nueva}')
print(F'Nueva Pares:{lista_pares_}')
print(sum(lista_pares_))