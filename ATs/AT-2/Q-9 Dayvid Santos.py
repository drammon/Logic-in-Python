while True:
    num1 = int(input("Para descobrir qual o maior de três (03) números inteiros, insira o primeiro: "))
    num2 = int(input("insira o segundo: "))
    num3 = int(input("insira o terceiro: "))

    if (num1 < num2):
        maior = num2
    elif (num2 < num1):
        maior = num1

    if (maior < num3):
        maior = num3
    else:
        maior == maior

    print(f"O maior dos números inseridos é o: {maior}.")
    
    escolha = input("Quer continuar com outra verificação? (sim/não): ").lower()
    
    if escolha != "sim":
        break

