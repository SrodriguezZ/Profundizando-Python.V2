#profundizando lista

nombre = ['Ing','Steeven','Rodríguez']
lenguaje = 'Python Java Kotlin'.split( )
#uniendo lista
print(nombre+lenguaje)
#extender una cadena 
nombre.extend(lenguaje)
print(f'Extender la lista1:{nombre}') 
#encontrar el indice
num = [1,2,3,4,5,6]
print(num.index(2))
#reverso de una lista
num.reverse()
print(f'Reverso:{num}')
#ordernar lista
num = [6,9,7,8,4,2,10,1]
'''num.sort()
print(num)
'''
#ordenar de manera descendente
num.sort(reverse=True)
print(f'Ordenar de manera descendente: {num}')
#obtener el valor min y max
print(min(num))
print(max(num))
#copiar elementos de una lista
z = [10,11]
x = z.copy()
print(x)
'preguntar si es el mismo contenido '
print(f'Es el mismo contenido: {x == z}')
#copiar con splicing
splicing = x[:]
print(splicing==x)
#MuMultiplicación de una lista
numMultiplicar = 5*[[2,5]]
print(numMultiplicar)
print(numMultiplicar[0]is numMultiplicar[2])
print(numMultiplicar[0]== numMultiplicar[2])
numMultiplicar[2].append(10)#comparten la misma memoria por esa razón se copia en toda la lista
print(numMultiplicar)
#Matriz en lista
matriz = [[10,25],[20,35,58],[50,60]]
print(f'Matriz columna 2 : {matriz[1][2]}')
#modificar el reglón de matriz
matriz[2][0]=27
print(f'modificar:{matriz}')
#ordenar una lista-matriz
num = [[3,2,1],[6,5,4],[9,8,7,6,5,4]]
#ordenar lista especifica
num[2].sort()
print(f'ordenar:{num}')
#ordenamiento por num de indice de la lista
num.sort(key=len)
print(num)
#REVERSE Y SORTED
'REGRESA ORDENADO SORTED'
num = [5,4,3,2,8,9,1,7,10]
carácter = ['a','c','d','e','b']
#ordenar de manera reversa por el metodo REVERSE= TRUE
num1 = sorted(num, reverse=True)
print(num1)
#REGRESA DE MANERA ORDENADA PERO CON LEN DEPENDIENTE EL CARACTER
carácter = sorted(carácter, key=len)
print(carácter)
#REGRESA CARACTERES LO CUAL TOCA CONVERTIR A UNA LISTA
num2 = reversed(num)
print(list(num2))


