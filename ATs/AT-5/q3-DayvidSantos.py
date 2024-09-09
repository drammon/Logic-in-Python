entrada = input("")
vet = [int(num) for num in entrada.split()]

if len(vet) == 18:
    matrix = [vet[i:i + 6] for i in range(0, 18, 6)]

for row in matrix:
    print(row)
