
# leer sobre url(https://python-docs-es.readthedocs.io/es/3.10/howto/urllib2.html)
import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read().decode("utf-8")
   print(html)

for palabra in html:
   palabras = palabra.decode('utf-8').split()
print(palabras)
#Método Guardar
'''with open("GuardaUrl.txt", "w",encoding="utf-8") as guardar:
    guardar.write(html)
'''
'''import urllib.request

with urllib.request.urlopen("http://globalmentoring.com.mx/recursos/GlobalMentoring.txt'") as url:
    web = url.read()
    print(web)'''

'''import urllib.request

req = urllib.request.Request('http://globalmentoring.com.mx/recursos/GlobalMentoring.txt')
with urllib.request.urlopen(req) as response:
   the_page = response.read()
   print(the_page)'''