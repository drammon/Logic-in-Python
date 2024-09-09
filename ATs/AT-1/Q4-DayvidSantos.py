preco=float(input())
desc= float(input())
descTotal = preco * (desc/100)
valorTotal= preco - descTotal
print (f"R${descTotal:.2f}")
print(f"R${valorTotal:.2f}")