
class lista_simple():

    def __init__(self, elementos) -> None:
        self.elementos = elementos 
    #agregar elementos
    def agregar(self,elemento):
        self.elementos.append(elemento)
    #retornar el elemento indicado
    def __getitem__(self,indice):
        return self.elementos[indice]
    #largo de nuestro elemento
    def largo(self,):
        return len(self.elementos)
    #ordenar
    def ordenar(self):
        return self.elementos.sort()
    def __repr__(self) -> str:
        return f'({self.__class__.__name__}({self.elementos!r}))'

#Clase que hereda de la clase padre

class lista_ordenada(lista_simple):

    def __init__(self, elementos=[]) -> None:
        super().__init__(elementos)
        #ordenamos lista
        self.ordenar()
    def agregar(self,elemento):
        super().agregar(elemento)
        self.ordenar()

#Validar con una clase que sea una lista de numeros enteros
class Lista_Entero(lista_simple):
    def __init__(self, elementos=[]) -> None:
        for elemento in elementos:
            self._validar(elemento)
        super().__init__(elementos)

    def _validar(self,elemento):
        if not isinstance(elemento, int):
            raise ValueError(f'No es un numero entero:{elemento}')
    
    def agregar(self,elemento):
        self._validar(elemento)
        super().agregar(elemento)


lista =  lista_ordenada([8,5,2,3,6,4,7,1,9])
print(lista)
lista.agregar(3)
print(lista)
print(lista.largo())

listaint = Lista_Entero([3,2,1,])
listaint.agregar(6)
print(listaint)


class Numeros_enteros(lista_simple):
    def __init__(self, elementos) -> None:
        super().__init__(elementos)
        for elemento in elementos:
            self._validar(elemento)

    def _validar(self, elemento):
        if not isinstance(elemento, int):
            raise ValueError(f'No es un numero entero:{elemento}')
    
    def agregar(self,v):
        super().agregar(v)
        self.ordenar()

x = Numeros_enteros([9,5,10,7,42])
print(x.largo())
print(x)
x.agregar(3)
print(x.__getitem__(1))
print(x)
print(Numeros_enteros.__mro__)
y = 5
x = Numeros_enteros([9,5,10,7,42])

#Utilizar Isinstance nos ayudar evaluar si una sentencia es igual 

print('Es una lista',isinstance(x,list))
print('Es un str',isinstance('s',str))