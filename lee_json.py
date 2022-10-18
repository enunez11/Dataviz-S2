import json


mi_json = open("datos2.json","r", encoding="UTF-8")

print(mi_json)

json_datos =mi_json.read()

datos = json.loads(json_datos)

print("json_datos", json_datos)
print("datos", datos)
print("temperatura", datos["temperatura"])