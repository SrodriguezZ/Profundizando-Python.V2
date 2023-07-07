
class Datos:
    #atributo de la clase
    contador = 0
    def __init__(self,nombre,apellido) -> None:
        self.nombre= nombre
        self.apellido = apellido
datos1 = Datos("Steeven","Rodríguez")
print(datos1.__dict__)
#Accediendo al atributo de la clase
print(datos1.contador)
#No es posible modificar con el objeto, sino con la clase
#crear un atributo al vuelo a la clase
datos1.contador =10
print(datos1.contador)
print(datos1.__dict__)
#Acceder al atributo de objeto
#print(datos1.contador)
#Acceder al atributo de la clase
#print(Datos.contador)
datos2 = Datos('Kyra','Zhunio')
#Podemos crear atributos de objetos de nuestra clase
Datos.contador2 = 50
print(datos2.contador2)
#Crear atributos al vuelo
datos2.Carrera = 'Ing'
print(datos2.__dict__)

#-----
#Crear atributos al vuelo
datos3 = Datos('Pedro','Perez')
datos3.carrera = 'Nutricion'
print(datos3.__dict__)
#crear un objeto dentro de mi clase
Datos.contador = 'gato'
print(Datos.__dict__)
