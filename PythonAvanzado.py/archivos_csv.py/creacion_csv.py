import csv

columnas =["Alejandra", 25, "Maravilla"]


datos=[
    ["Alfonso", 25, "Maravilla"],
    ["Laura", 25, "Maravilla"],
    ["Jose", 25, "Maravilla"],
    ["Enrique", 25, "Maravilla"]
]

x=0
while x <=3:
    x +=1
    with open(f'datos{x}.csv', 'w') as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(columnas)
        writer.writerows(datos)
