#Multiplicación de cadena
lista = 5*[0]

print(f'Lista: {lista} Largo:{len(lista)}')

mensaje = 'Hola \'Mundo' # se debe poner \ para se valido'
print(f'Resultado : {mensaje}')

mensaje = 'c:\\nuevo\\mundo' # se debe poner \\ para se valido \
print(f'Resultado : {mensaje}')
#row string
mensaje = r'c:\nuevo\mundo' # se debe poner roR(row string) para se valido \
print(f'Resultado : {mensaje}')

#UNICODE
mensaje = '\u006b'
print(f'Resultado : {mensaje}')
print('Trébol:', '\U0001F340')
print('Serpiente:', '\U0001F40D')

#Carácter Ascii
carácter = chr(65)
print(f'Ascii: {carácter}')
carácter = chr(64)
print(f'Ascii: {carácter}')

#byte - carácter|
by = b'Hola Mundo'
print(by[0])
print(chr(by[0]))

#Str a Byte
string = "Ing Software Steeven Rodríguez"
byte = string.encode("utf-8")
print(byte)

# Byte a str -cadena
byte2 = byte.decode("utf-8")
print(byte2)

#PROFUNDIZANDO STR

txt = '''
En GlobalMentoring.com.mx ofrecemos cursos online para que te conviertas en el profesional que siempre has deseado.

Nuestro listado de cursos incluyen:
1. Universidad Python
2. Universidad Java
3. Universidad Excel
4. Universidad Desarrollo Web - Front End Developer
5. Universidad JavaScript
6. Universidad Angular
7. Universidad Spring

Entre muchos temas más.

Te invitamos a inscribirte ya mismo.

Tu amigo e instructor

Ing. Ubaldo Acosta
Fundador de GlobalMentoring.com.mx
'''
#COUNT - BUSCA CUANTAS VECES SE REPITE - CAPITALIZE (PRIMERA EN MAYúSCULA )
print(txt.count("Universidad".capitalize()))
#lower-minúscula-upper(mayúscula)
print(txt.lower())
#startswith(Comienza con) endswith(termina con )
txt1 = 'Steeven Rodríguez'
print(txt1.startswith("S"))
print(txt1.lower().endswith("Rodríguez".lower()))
#buscamos la cadena python en el txt
print("Existe la palabra python ?:", "python".lower() in txt.lower())
#Preguntar si esta en mayúscula o minúscula
print(txt1.lower().islower())
#Mutar - revisar(http://elclubdelautodidacta.es/wp/2012/11/python-mayusculas-minusculas-y-viceversa/)
m = txt1[:2]+txt1[2].upper()+txt1[3:]
print(m)
#Alinear Cadena
txt3 = "Ing Software Steeven Rodríguez"
print(len(txt3))
print(txt3.center(100,"*"))#Coloca el carácter si la cadena no esta llena 
print(len(txt3.center(50,"*")))#rellena los carácter por si falta en numero
print(txt3.center(len(txt3)+10,"*"))# centrar el texto con la mitad de cada carácter dado
#Centrar a la izq
print(txt3.ljust(50,"*"))#Completa con las letras *
print(txt3.ljust(len(txt3)+50,"*"))#Completa con 50 * para alinear
#Centrar a la derecha
print(txt3.rjust(len(txt3)+50,"-"))
#Utilizando el método replace y strip
txt3 = " ***Ing Software Steeven Rodríguez*** "
print(txt3.replace(" ","-"))
#strip
print(txt3)
print(txt3.strip(" ").strip("*"))#podemos aplicar el mismo strip para seguir eliminando elementos 
#eliminar elementos hacia la izq o der
print(txt3.lstrip(" ").lstrip("*"))
print(txt3.rstrip(" ").rstrip("*"))

#PRUEBA 
'''s = input()
x = 0
for i in s:
    x+= ord(i)
print(x)
'''
#map con ord 
#print(sum(map(ord,input())))
#lista str a list int con map
'''lista_de_cadenas = ["5","6","7","8","9", "10"]
resultado = map(int,lista_de_cadenas)
print(list(resultado))
'''
code_string = "print('Hello, word.!')"
eval(code_string)

'''t1 = ([1],[2],[3])
t1[0][0] = 0
print(t1)
print(int(input())*2**6)'''
texto = "Programación Python"
#desempaquetando cadena
valor, valor2, valor3 = 1,2,3
print(valor,valor2,valor3)
valor1,*valor2 = 1,2,3
print(valor1, valor2)
def num ():
    return 1,2,3
x = valor1,*valor2= num()
print(x)
x = hora, minuto, segundo = "6:34:56".partition(":")
print(hora,minuto, segundo)
print(len(x))