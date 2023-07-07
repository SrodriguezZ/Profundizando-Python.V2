

import inspect


def decorador_clase(cls):
    print('Iniciando decorador de la clase')
    print(f'Decorador de la clase{cls.__name__}')

    #Revisamos los atributos de la clase con el método vars
    atributos = vars(cls)
    #for nombre, atributo in atributos.items():
    #    print(nombre,atributo)
    #Revisamos si se ha sobrescrito el método __init__

    if '__init__'not in atributos:
        raise TypeError (f'Error del atributo:{cls.__name__}')
    
    #Firma del método init con eso validamos los elementos de nuestra clase
    firma_init = inspect.signature(cls.__init__)
    print(f'Firma método __init__:{firma_init}')

    #Recuperamos los parámetros excepto self
    parámetros__init__=list(firma_init.parameters)[1:]
    print(f'Parámetros:{parámetros__init__}')

    #Revisemos si en los método tenemos un property
    for parámetro in parámetros__init__:
        método_property = isinstance(atributos.get(parámetro),property)
        if not método_property:
                raise TypeError('Error')

    return cls




@decorador_clase
class Persona():

    def __init__(self, nombre, apellido) -> None:
        self._nombre = nombre
        self._apellido =  apellido

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def apellido(self):
        return self._apellido
    
persona = Persona('Steeven','Rodriguez')