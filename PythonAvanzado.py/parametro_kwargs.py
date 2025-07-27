def parametro_kwargs(**kwargs):
    diccionario = kwargs
    for x in diccionario.values():
        diccionario = x

    return diccionario

resultado = parametro_kwargs(nombre ="Jhon")

print(resultado)

