graus = input("")

temperaturas = [int(n) for n in graus.split()]

def nomeMes(i):
    match i:
        case 0:
            return "JANEIRO"
        case 1:
            return "FEVEREIRO"
        case 2:
            return "MARÇO"
        case 3:
            return "ABRIL"
        case 4:
            return "MAIO"
        case 5:
            return "JUNHO"
        case 6:
            return "JULHO"
        case 7:
            return "AGOSTO"
        case 8:
            return "SETEMBRO"
        case 9:
            return "OUTUBRO"
        case 10:
            return "NOVEMBRO"
        case 11:
            return "DEZEMBRO"
        
maior = 0
maiorMes = []
menor = 0
menorMes = []

for i, e in enumerate(temperaturas):
    if e > maior:
        maior = e
        maiorMes= i
    elif e <= menor:
        menor = e
        menorMes = i

print(f"MAIOR: {maior}C° em {nomeMes(maiorMes)}")
print(f"MENOR: {menor}C° em {nomeMes(menorMes)}")