import urllib.request
import json
url ="http://globalmentoring.com.mx/api/clima.json"
petición = urllib.request.Request(url,data=None,
    headers={
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    })

cuerpo_http = urllib.request.urlopen(petición)
print(cuerpo_http)
json_mostrar = cuerpo_http.read()
mostrar_json = json.loads(json_mostrar.decode("utf-8"))
print(mostrar_json)
#SSe forma un diccionario lo cual debemos sacar el primer elemento 
clima = mostrar_json["clima"][0].get("principal")
print(clima)
principal = mostrar_json["principal"].get("temp_min")
print(principal)
    

