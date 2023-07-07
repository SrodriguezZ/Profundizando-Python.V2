#Funcion Zip

num = [1,2,3]
tupl = ('a','b','c','d')
seT = {'hola','mundo','moure','dev'}
resultado = zip(num,tupl,seT)
print(list(resultado))
#ITERAR ZIP - se debe ponenr el formato zip en el for para poder iterar
nueva_lista = []
for numero,caracter, palabras in zip(num,tupl, seT):
    nueva_lista.append(f'{numero}-{caracter}-{palabras}')
print(nueva_lista)
#unzip
datos = [(1,'a'),(2,'b')]
numeros, letras = zip(*datos)
print(f'Numeros:{numeros} Letras:{letras}')
#ordenar 
numero = [2,3,1]
letra = ('a','b','c')
print(sorted(zip(numero,letra)))
#crear diccionario
llave = ['Nombre','Apellido']
clave = ['Steeven','Zhunio']
dicc = dict(zip(llave, clave))
print(dicc)
'Actualizar'
llave = ['Nombre']
clave = ['David']
dicc.update(zip(llave,clave))
print(dicc)
#prueba
prueba = 'HOLA MUNDO'
resultado = list(reversed(prueba))
print("".join(resultado))
prueba2 = 'HOLA, MUNDO'

