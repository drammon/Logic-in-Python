def potencia(x, z):
    return x**z

string = input("")

valores = [int(i) for i in string.split()]

result = potencia(valores[0], valores[1])

print(result)