# parametros args
# Captura múltiples argumentos posicionales como una tupla

def calacular_perimetro(*args):
    print(type(args))
    perimetro=0
    for x in args:
        perimetro +=x
    return perimetro
perimetro = calacular_perimetro(1,2,3,4)
print(type(perimetro))


