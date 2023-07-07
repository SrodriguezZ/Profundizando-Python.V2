#Definimos una variable global

contador = 0

def mostrar_contador():
    print(contador)

def cambiar_contador(c):
    #para llamar a mi variable global debo asignar dicha palabra global
    #ya que el interpretador me agarra como una variable nueva
    global contador
    contador =  c
    print(contador)

mostrar_contador()
cambiar_contador(5)