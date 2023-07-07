
#Podemos utilizar para trabajos pequeños

from dataclasses import dataclass
from typing import ClassVar

#eq=para apuntar al mismo espacio de la memoria
#Frozen para que sean inmutable, si ponemos tru ya no podemos modificar
@dataclass
class Domicilio(eq=True, frozen=True):
    dirección: str
    numero: int = 0

@dataclass
class Persona(eq=True, frozen=True):

    nombre: str
    apellido: str
    domicilio: Domicilio
    contador_personas: ClassVar[int]


    #podemos validar si el valor de la instancia esta vació nos marcara un error
    def __post_init__(self):
        if  not self.nombre:
            raise ValueError(f'Error')

persona = Persona('Steeven','Rodriguez',None)
persona2 = Persona('s','',None)
print(f'{persona!r}')# método repr
print(persona2)
persona3 = Persona('David','Zhunio',Domicilio('X',50))
print(persona3)
coleccion = {persona3,persona3}

