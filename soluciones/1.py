def suma_digitos(numero):
    suma = 0

    while numero > 0:
        digito = numero % 10
        suma += digito
        numero = numero // 10
    return suma
      
     
numero = int(input("Introduce un numero: "))
resultado = suma_digitos(numero)
print(f"la suma de los digitos de: {numero} " +
      f"es: {resultado}")