valor_a = int(input("digite o valor da base: "))

valor_b = int(input("digite o valor do expoente : "))


if valor_b == 1:
    valor_total = valor_a
    print(valor_total)
    
else:
    valor_total = valor_a * valor_a

    for i in range(2,valor_b):
    
        valor_total = valor_total * valor_a
        valor_total = valor_total
    print(valor_total)
    