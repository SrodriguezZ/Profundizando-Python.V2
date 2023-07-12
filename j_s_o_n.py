import urllib.request
import json

url = 'http://globalmentoring.com.mx/api/personas.json'
petición = urllib.request.Request(url,data=None,
headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})

repuesta = urllib.request.urlopen(petición)
print(repuesta)
#Cuerpo del http
cuerpo = repuesta.read()
print(cuerpo)
#Procesamos la repuesta 
cuerpo_mostrar = json.loads(cuerpo.decode("utf-8"))
print(cuerpo_mostrar)
#imprimir solo los nombre de las personas 
#json se convierte en lista y diccionario en python
#Iteramos con un for cuando tenemos mas opciones en nuestro contenido como tipo diccionario
for personas in cuerpo_mostrar["personas"]:
    
    print(f"{personas['nombre']}{personas['edad']}")
#si queremos retomar un valor exacto podemos utilizar el json
print(cuerpo_mostrar["mensaje"])
print(cuerpo_mostrar.get("total"))



