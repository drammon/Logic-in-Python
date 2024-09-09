
while True:
    salario = float(input("Para saber qual será o reajuste do salário, insira o valor a seguir (caso seja um valor decimal, utilizar '.' para designar as casas decimais): "))
    
    while True:
        if (salario <= 0.00):
            salario = float(input("O salário não pode ser menor ou igual a 0. Insira novamente:"))
        else:
            break

    if (salario <= 1212.00):
        salario = salario + (salario * 0.2)
        
    else:
        salario = salario + (salario * 0.15)     

    print(f"Com o reajuste seu salário ficará em R${salario:.2f}.")

    escolha = input("Quer continuar com outro cálculo de reajuste? (sim/não): ").lower()
        
    if escolha != "sim":
        break