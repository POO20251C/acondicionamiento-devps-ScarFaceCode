def contar_vocales(cadena):
    contador = 0
    vocales = "aeiouAEIOU"
    for caracter in cadena:
        if caracter in vocales:
            contador += 1
    print(contador)