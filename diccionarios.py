import random
#Diccionario 
'''import random
datos = {'Carrera':'Ingeniero','Nombres':'Steeven David','Edad':27}
print(datos['Carrera'])
print(datos.setdefault('Mascota','Kyra'))
print(datos)
print(datos.get('Nombre','No se encuentra'))'''




##nombres

datos = ['Robinson Peralta ','Steeven Rodríguez','Kevin Vargas','Joe Guerra','Nelson Montes','Julio Davíla','Darwin Garcia']
aleatorio = random.sample(datos,1)
print(f'**********GANADOR:{aleatorio}*********')
# print(datos[aleatorio])

#frutas = ['peras', 'manzanas', 'plátanos', 'ciruelas']
#for i in range(0,2):
# print(random.randint(frutas))