precoFabrica = float (input("Digite o preço d fabrica: "))
if precoFabrica >= 0 and precoFabrica <35000:
    precoFinal = precoFabrica * 0.05 + precoFabrica
    print (precoFinal)
elif precoFabrica>= 35000 and precoFabrica <= 70000:
    precoFinal = (precoFabrica * 0.10) + (precoFabrica*0.15) + precoFabrica
    print (precoFinal)
else:
    precoFabrica > 70000
    precoFinal = (precoFabrica*0.15)+(precoFabrica*0.20)+precoFabrica
    print (precoFinal)