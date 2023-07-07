#Profundizando tuplas
#Variable

a,b = "HOla","MUNDO"
print(a,b)
b,a = a,b
print(b,a)
#Funcion 
def suma(elementos):
    return min(elementos), max(elementos)
suma = suma((1,2,3,4,5,6,7))
print(suma)
#Funcion suma
def suma(*args):
    return sum(*args)
sumas=suma([1,2,3,4,5])
print(sumas)