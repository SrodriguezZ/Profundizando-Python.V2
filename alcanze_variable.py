#Alcance de variable

var_global = 'Ing Steeven Rodríguez'

def Variable_global():
    global var_global
    print(f'Variable global:{var_global}')

    variable_local = "Ing. Zhunio"
    var_global = "variable global"

    def var_local():
        print(f'Variable local:{variable_local}')
    var_local()

    def var():
        print(f'Funcion anidada: {var_local}')

Variable_global()

# NO podemos llamar una variable local fuera de Funcion print(variable_local)