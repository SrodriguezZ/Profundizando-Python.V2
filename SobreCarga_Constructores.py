#En python no creamos en si sobrecarga de constructores, pero existe otras formas de crear elementos 
class Datos:

    def __init__(self,nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido

    @classmethod
    def objetos_vacíos(cls,):
        return cls(None,None)
    def __str__(self) -> str:
        return f'Nombre:{self.nombre} Apellido:{self.apellido}'

datos = Datos('Steeven','Rodríguez')
print(datos)
datos_vacíos = Datos.objetos_vacíos()
print(datos_vacíos)

class MarcasPc:

    def __init__(self, marca) -> None:
        self.marca = marca
    
    #Crear algo similar a constructor de la clase para poder tirar null 
    @classmethod
    def vació(cls):
        return cls(None)
    def __str__(self) -> str:
        return f'Marca:{self.marca}'

marca1 = MarcasPc('Lg')
print(marca1)

marca2 = MarcasPc.vació()
print(marca2)