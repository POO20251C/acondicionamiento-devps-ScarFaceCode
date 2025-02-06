def es_palindromo(cadena):
    nueva_cadena = ""
    for caracter in cadena:
        if caracter != " ":
            nueva_cadena += caracter.lower()
    if nueva_cadena == nueva_cadena[::-1]:
        print("Sí")
    else:
        print("No")