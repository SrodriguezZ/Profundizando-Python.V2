

def función_decorada_a(función_decorada_b):
    def función_Decorada_c():
        función_decorada_b()
    return función_Decorada_c

@función_decorada_a
def mostrar_mensaje():
    print("Ing Steeven Rodríguez")
mostrar_mensaje()


def operaciones(operacionesb):
    def operacionesc(*args,**kwargs):
        operacionesb(*args,**kwargs)
    return operacionesc
@operaciones
def suma(a,b):
    return a+b
    print("Ing Zhunio")

x = suma(5,5)
print(x)