#Atributos publico, protegido,privado

class Atributos:
    def __init__(self, valor_publico, valor_protegido,valor_privado) -> None:
        self.public = valor_publico
        self._protegido = valor_protegido
        self.__privado = valor_privado

objecto = Atributos('V_P','V_PRO','V_PRI')
print(objecto.public)
print(objecto._protegido)
#De esta manera podemos acceder atributo a privado pero no deberiamos 
print(objecto._Atributos__privado)

