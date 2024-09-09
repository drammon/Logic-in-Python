grupo = []
pares = []
impares = []

for i in range (6):
    num = int(input())
    grupo.append(num)


for e in grupo:
    if e % 2 == 0:
        pares.append(e)
    else:
        impares.append(e)

qpares = len(pares)
qimpares = len(impares)

print(qpares, " pares. São eles:")
for e in pares:
    print(e)

print(qimpares, " ímpares. São eles:")
for e in impares:
    print(e)

