
#un closure es una función que defina a otra, y ademas la regresa
'''def operaciones(a,b):
    #
    def sumar():
        return a+b
    return sumar
'''

def operaciones(a,b):
    return lambda:a+b
resultado = operaciones(5,5)
print(resultado())
#llamar la función al vuelo
print(f'Función al vuelo:{operaciones(5,5)()}') 
