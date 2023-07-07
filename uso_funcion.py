#definir mi función
def sumar(a,b):
    return a+b
#guardo mi función dentro de una variable 
mi_función = sumar
#saber el tipo de mi función
print(type(mi_función))
#llamar a la función
print(mi_función(5,5))
#llamar una función como argumento
def argumentos(a,b,sumar_arg):
    print(f'Sumar argumentos:{sumar_arg(a,b)}')
argumentos(5,10,sumar)
#retornar un función
def retorno():
    return sumar
retorno_función = retorno()
print(f'Argumentos de retorno:{retorno_función(10,10)}')

def for_each(item_in, do):
    for item in item_in:
        do(item)

languages = ["Java", "C", "C++", "Elixir"]
for_each(item_in=languages, do=print)

def datos(datos,imprimir):
    for i in datos:
        imprimir(i)

usuario = ["Ing","Steeven","Rodríguez"]
datos(datos=usuario,imprimir=print)