preco = float(input(""))
venda = int(input(""))

if venda < 500 and preco < 30.00:
    percentual = 0.10 * preco
    print(preco + percentual)

elif venda >= 500 and venda < 1200 and preco >= 30.00 and preco < 80.00:
   percentual = 0.15 * preco
   print(preco + percentual)

elif venda >= 1200 and preco >= 80.00:
    percentual = 0.20 * preco
    print(preco - percentual)
    