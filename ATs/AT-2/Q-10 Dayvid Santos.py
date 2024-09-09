import math
while True:
    print("\nCalculadora simples de três (03) operações: \n\n       1. O primeiro número elevado ao segundo; \n\n       2. A soma dos quadrados de cada um dos dois números; \n\n       3. A soma das raízes quadradas de cada um dos números.\n") 

    opcao = int(input("Para começar, insira a opção desejada: "))
    num1 = int(input("\nInsira o primeiro número: "))
    num2 = int(input("\nInsira o segundo número: "))
    
    
    match opcao:
        case 1:
            result = num1**num2
            print(f"\nO resultado é: {result:.1f}.")
        case 2:
            result = (num1**2) + (num2**2)
            print(f"\nO resultado é: {result:.1f}.")

        case 3:
            result = (math.sqrt(num1))+(math.sqrt(num2))
            print(f"\nO resultado é: {result:.1f}.")

        case _:
            print(f"\nErro! Você selecionou uma opção inválida!")

    escolha = input("\nQuer continuar com outra verificação? (sim/não): ").lower()
    
    if escolha != "sim":
        break