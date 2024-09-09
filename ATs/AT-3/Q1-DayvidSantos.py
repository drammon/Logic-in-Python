saldo_medio = float(input("digite o valor do seu saldo: "))


if saldo_medio > 0 and saldo_medio <= 200:
    aumento = saldo_medio * 10 / 100
    #saldo_medio = saldo_medio + aumento
    print( " seu credito concedido é R$:",aumento)
    
elif saldo_medio > 200 and saldo_medio <= 300:
    aumento = saldo_medio * 20 / 100
    #saldo_medio = saldo_medio + aumento
    print( " seu credito concedido é R$:", aumento)
    
    
elif saldo_medio > 300 and saldo_medio <= 400:
    aumento = saldo_medio * 25 / 100
    #saldo_medio = saldo_medio + aumento
    print( " seu credito concedido é R$:", aumento)
    
elif saldo_medio >400:
    aumento = saldo_medio * 30 / 100
    #saldo_medio = saldo_medio + aumento
    print( " seu credito concedido é R$ :", aumento)