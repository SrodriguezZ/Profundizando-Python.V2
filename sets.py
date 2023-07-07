#PROFUNDIZANDO SET
#Sets es una colección de elementos únicos y es mutable
#los elementos de un set deben ser inmutables
#sets no puede repetir los mismo valores 
sets = {1,2,3,4,5,6,7}
print(f'Sets:{sets}')
sets.add(10)
print(sets)
#set vació
sets = set()
print(type(sets))
#copiar set 
pelo = {'Negro','Amarillo','Azul','Verde'}
zapatos = {'Azul','Amarillo','Rojo'}
carro = {'Verde','Cafe','Amarillo'}
#union
print(pelo.union(carro))
#Intersección 
print(f'Devuelve lo que repite:{pelo.intersection(carro)}')
#diferencia
print(f'Devuelve lo de un conjunto A lo que no se repite: {pelo.difference(carro)}')
#simetrica
print(f'Devuelvo lo que no se encuentra en ambos conjuntosAYB{pelo.symmetric_difference(carro)}')
#subset
#devuelve si todo los elementos estan en la lista 
print(f'Ver si todo los elementos estan en la lista{pelo.issubset(carro)}')

print(f'Si el conjunto contiene otro conjunto o no: {pelo.issuperset(carro)}')

