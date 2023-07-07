
#No ponemos definir una lambada en una función

resultado = lambda a,b: a+b
print(f'Resultado:{resultado(5,5)}')
#sin argumento
resultado = lambda: "hola mundo"
print(f'Sin argumento: {resultado()}')
#con diccionario o tuple
resultado = lambda a,b,*args,**kwargs: a+b+len(args)+len(kwargs)
print(f'Resultado:{resultado(1,2,3,4,6, e=7,d =8)} ')
#lambada con valor asignado
resultado = lambda a,b,c=5:a+b+c
print(f'Resultado:{resultado(1,2,3)}')
