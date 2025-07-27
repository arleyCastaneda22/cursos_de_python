#Retorna un objeto iterable y me permite saber los indices de los iterabels

nombres =["Juana", "Alejnadra", "Laura"]


nombres_con_indice =enumerate(nombres, 5)

for indice, elemento in enumerate(nombres):
    print(indice, elemento)