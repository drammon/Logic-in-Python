soma = 0
while True:
    num = int(input(""))
    if num > 0:
        if num % 3 == 0:
            soma = soma + num
    else:
        print(soma)
        break


