def maximo_minimo(numeros):
    numero = ""
    lista = []
    for caracter in numeros:
        if caracter != " ":
            numero += caracter
        else:
            if numero:
                lista += [int(numero)]
                numero = ""
    if numero:
        lista += [int(numero)]
    
    maximo = lista[0]
    minimo = lista[0]
    for num in lista:
        if num > maximo:
            maximo = num
        if num < minimo:
            minimo = num
    print(maximo, minimo)