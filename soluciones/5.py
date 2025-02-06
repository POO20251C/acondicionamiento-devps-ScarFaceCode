def contar_palabras(cadena):
    palabra = 0
    en_palabra = False
    for caracter in cadena:
        if caracter != " ":
            if not en_palabra:
                palabra += 1
                en_palabra = True
        else:
            en_palabra = False
    print(palabra)