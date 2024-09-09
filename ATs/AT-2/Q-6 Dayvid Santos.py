while True:
    num1 = int(input("Para descobrir se dois números são múltiplos, digite o primeiro: "))
    num2 = int(input("Digite o segundo: "))

    if num1 == 0 or num2 == 0:
        print("Os números não são múltiplos.")
    else:
        if num1 % num2 == 0 or num2 % num1 == 0:
            print("Os números são múltiplos.")
        else: 
            print("Os números não são múltiplos.")
    
    escolha = input("Quer continuar com outra verificação? (sim/não): ").lower()
    
    if escolha != "sim":
        break