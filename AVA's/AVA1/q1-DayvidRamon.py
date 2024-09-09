codigo = int(input(""))
salario = int(input(""))

match codigo:
    case 1:
        print("Escrituário")
        percentual = salario * 0.50
        print(percentual)
        salarionovo = salario + percentual
        print(salarionovo) 
    case 2: 
        print("Secretário")
        percentual = salario * 0.35
        print(percentual)
        salarionovo = salario + percentual
        print(salarionovo)
    case 3:
        print("Caixa")
        percentual = salario * 0.20
        print(percentual)
        salarionovo = salario + percentual
        print(salarionovo)
    case 4:
        print("Gerente")
        percentual = salario * 0.10
        print(percentual)
        salarionovo = salario + percentual
        print(salarionovo)
    case 5:
        print("Diretor")
        print("Não tem aumento")
        print(salario)