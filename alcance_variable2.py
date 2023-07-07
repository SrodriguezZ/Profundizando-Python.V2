
def variable_externa():

    variable_externa = " variable externa"

    def variable_interna():
        variable_interna = "variable interna"

        nonlocal variable_externa #con esto podemos llamar la variable
        variable_externa = "Nueva variable externa"
    variable_interna()
    print(f'Variable interna:{variable_externa}')
variable_externa()