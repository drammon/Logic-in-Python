entrada = input("")
lista = [int(num) for num in entrada.split()]


def eh_Primo (num):
    divisores = 0

    for i in range (1, (num + 1)):
        if num % i == 0:
            divisores += 1
    
    if divisores == 2:
        return True
    else:
        return False
    
for i, num in enumerate(lista):
    if eh_Primo(num) == True:
        print (num, i)

