#Funcion anidada

def calculadora(a,b, operaciones=None):

    def sumar(a,b):
        return f'Sumar:{a+b}'
    
    def restar(a,b):
        return f'Restar:{a-b}'
    
    if(operaciones=='sumar'.upper()):
        print(sumar(a,b))
    elif (operaciones=='restar'.lower()):
        print(restar(a,b))

calculadora(5,10, 'SUMAR')
    