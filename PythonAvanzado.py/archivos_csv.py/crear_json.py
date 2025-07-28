import json

persona ={
    "Nombre": "Alejo",
    "Apellido":"Ailicia maravilla",
    "Edad" : 24
}

json =json.dumps(persona, indent=2)

with open("persona.json", "w")as file_json:
    file_json.write(json)


