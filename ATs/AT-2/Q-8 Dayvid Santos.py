while True:
    nota1 = float(input("Para calcular a média aritmética das suas notas, insira a seguir a primeira nota: "))
    nota2 = float(input("Insira a segunda nota: "))

    media = (nota1 + nota2)/2

    print(f"A média das suas notas é: {media:.1f}")
    
    escolha = input("Quer continuar com outro cálculo de média? (sim/não): ").lower()
    
    if escolha != "sim":
        break