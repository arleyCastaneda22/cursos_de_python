import csv

columnas =["Alejandra", 25, "Maravilla"]


datos=[
    ["Alejandra", 25, "Maravilla"],
    ["Alejandra", 25, "Maravilla"],
    ["Alejandra", 25, "Maravilla"],
    ["Alejandra", 25, "Maravilla"]
]

x=0
while x <=3:
    x +=1
    with open(f'datos{x}.csv', 'w') as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(columnas)
        writer.writerows(datos)
