entrada1 = input("")
lista1 = [int(num) for num in entrada1.split()]
entrada2 = input("")
lista2 = [int(num) for num in entrada2.split()]
lista = lista1 + lista2

seen = set()
listaFinal = []

for e in lista1:
    if e not in seen:
        seen.add(e)
        listaFinal.append(e)

for e in lista2:
    if e not in seen:
        seen.add(e)
        listaFinal.append(e)
    
print(listaFinal)