grupo = []
multiplos_2 = []
multiplos_3 = []
multiplos_2e3 = []

for i in range(7):
    num = int(input())
    grupo.append(num)

for e in grupo:
    if e % 2 == 0 and e % 3 == 0:
        multiplos_2e3.append(e)
    elif e % 2 == 0:
        multiplos_2.append(e)
    elif e % 3 == 0:
        multiplos_3.append(e)

print("São múltiplos de 2: ")
for j in multiplos_2:
    print(j)

print("São múltiplos de 3: ")
for j in multiplos_3:
    print(j)

print("São múltiplos de 2 e 3: ")
for j in multiplos_2e3:
    print(j)
