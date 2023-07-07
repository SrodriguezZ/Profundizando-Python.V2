numero = [1,2,3]

print(*numero, sep=" - ")

#Desempaquetando al momento de pasar un parámetro en una la función
def suma(a,b,c):
    print (f"suma:{a+b+c}")
suma(*numero)
#Extraer unas parte de la lista
numeros = [1,2,3,4,5,6,7,8]
a,*b,c,d = numeros
print(a,b,c,d)
#diccionario desempaquetando
dicc1 = {'A':1,'B':2,'C':3}
dic2 = {'D':4,'E':5,'F':6}
dic3 = {**dicc1,**dic2}
print(dic3)
# Str
datos = [*'Ing Software Steeven Rodríguez']
print(datos)
print(*datos)
print(*datos, sep="")