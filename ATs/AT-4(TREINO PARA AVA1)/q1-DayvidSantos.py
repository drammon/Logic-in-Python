soma = 0 

while True:
    num = int(input())
    if num > 0:
        div = 0
        for i in range (1, num+1):
            if num % i == 0:
                div += 1 
        if div == 2:
            soma += num
    else: 
        print (soma)
        break

    