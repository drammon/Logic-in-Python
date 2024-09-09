valor1 = float(input('Valor 1'))
valor2 = float(input('Valor 2'))
valor3 = float(input('Valor 3'))
triangulo = ""
soma = valor1 + valor2 + valor3


if soma == 180:
    
    if valor1 == 90 or valor2 == 90 or valor3 == 90:
        triangulo = "triangulo retangulo"
        print('as somas dos angulos é igua a: ' , triangulo)
        
    elif valor1 > 90 or valor2 > 90 or valor3 > 90:
        triangulo = "Triangulo obtusangulo"
        print('as somas dos angulos é igua a: ' , triangulo)

    elif valor1 < 90 and valor2 < 90 and valor3 < 90:
        triangulo = "Triangulo acutangulo"
        print('as somas dos angulos é igua a: ' , triangulo)
else:
    print('A soma total deve ser no max 180')
