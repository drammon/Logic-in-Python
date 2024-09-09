valor_linhas = int(input("digite o valor de linhas: "))

valor_colunas = int(input("digite o valor de colunas : "))


for i in range(valor_linhas):
    linha = []
  
    for j in range(valor_colunas):
        linha.append("#")
    print(linha)
        
    print()