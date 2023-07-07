from map import map_argument_parser
'MÉTODO STR CON JOIN'
'JOIN - UNIR '
tuple = ('HOLA','MUNDO')
N_tuple = ' '.join(tuple)
print(f'JOIN : {N_tuple}')
print(type(tuple))
print(type(N_tuple))
print(len(N_tuple))


diccionario = {'HOLA':'MUNDO','JAVA':'SPRING'}
N_diccionario = ' '.join(diccionario.keys())
print(f'Clave: {N_diccionario}len:{len(N_diccionario)}')
print(type(diccionario))

'STR - SPLIT - SEPARA'
lista = 'Hola mundo como estas'
N_lista = lista.split( )
print(f'Split1: {N_lista} Elementos:{len(N_lista)}')
x = list(map(str.capitalize, N_lista))
print(x)

lista1 = 'Hola, Mundo, Como , Estas, Steeven'
N_lista1 = lista1.split(', ')
print(f'Split2: {N_lista1} Elementos:{len(N_lista1)}')

datos = 'Ing Steeven Rodriguez'
print(len(datos))
datos1 = datos.split(' ')
mapeo = (list(map(str.lower, datos1)))
print(datos1)
print(f'Mapeo: {mapeo}')



datos2 = 'Ing Steeven Rodriguez'

Datos2 = datos2.split(' ')
print(f'Datos2:{Datos2}len:{len(Datos2)}')  
datos3 = ['Ing','Steeven','Rodriguez']
Datos3 = ' '.join(datos3)
print(Datos3)

'USO DEL MeTODO FORMAT'

cadena = 'nombre %s edad %d' %('Pedro',35)
print(cadena)
Carrera= 'Ing'
Nombre= 'Steeven'
edad= 35
sueldo = 1300.00
'FORMAT'
cadena2 = ' Carrera: {0} Nombre:{1} Edad: {2}'.format(Carrera,Nombre,edad)
print(cadena2)
diccionario = {'nombre':'Steeven','carrera':'Ing Software','sueldo':'1300.00'}
#mensaje='Nombre:{dic[nombre]} Carrera:{dic[carrera]} Sueldo: {dic[sueldo]}'.format(dic=diccionario)
print('Nombre:{dic[nombre]} Carrera:{dic[carrera]} Sueldo: {dic[sueldo]}'.format(dic=diccionario))
#sep
print(Carrera,Nombre,edad,sueldo,sep=' - ')

#Multiplicación de cadena
lista = 5*[0]

print(f'Lista: {lista} Largo:{len(lista)}')
