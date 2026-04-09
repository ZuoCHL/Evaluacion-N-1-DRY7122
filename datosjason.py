import json

with open ('myfile.json','r') as jason_file:
    ourjson = json.load(jason_file)

token = ourjson['access_token']
tiempo_deToken = ourjson ['expires_in']


print ("el valor del token es: " + token)
print("el tiempo del token antes de borrarse es de: " + str (tiempo_deToken) + "segundos.")