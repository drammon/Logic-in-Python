votosString = input("")

votos = [int(i) for i in votosString.split(", ")]

placar = [0, 0, 0, 0]
nulos = 0
brancos = 0

for i in votos:
    match i:
        case 1:
            placar[0] += 1
        case 2:
            placar[1] += 1
        case 3:
            placar[2] += 1
        case 4:
            placar[3] += 1
        case 5:
            nulos += 1
        case 6:
            brancos += 1

total = len(votos)

def calcPercent(num):
    return (num/total)*100

print(f"VOTOS = {total}")

for i, e in enumerate(placar):
    print(f"C#{i+1} = {calcPercent(e):.0f}%") 

print(f"NULOS = {calcPercent(nulos):.0f}%")
print(f"BRANCOS =  {calcPercent(brancos):.0f}%")

