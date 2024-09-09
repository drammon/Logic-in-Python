import math

a = int(input("Para descobrir qual o maior de três números, insira o primeiro: "))
b = int(input("Insira o segundo número: "))
c = int(input("Insira o terceiro número: "))

maior = (a+b+abs(a-b))/2
maior2 = (maior + c + abs(maior -c))/2

print(f"O maior valor é o: {maior2}")
