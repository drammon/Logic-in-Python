def correcaoProvas(inputDados):
    dados = inputDados.split()
    
    gabarito = dados[:10]
    
    numEstudantes = int(dados[10])
    
    respostasEstudantes = dados[11:]
    
    aprovados = 0
    
    for i in range(numEstudantes):
        inicio = i * 10
        fim = inicio + 10
        respostas = respostasEstudantes[inicio:fim]
        
        nota = sum(1 for j in range(10) if respostas[j] == gabarito[j])
        
        print(f"Aluno #{i + 1}: {nota}.0")
        
        if nota >= 6:
            aprovados += 1
    
    percentAprovavao = (aprovados / numEstudantes) * 100
    
    print(f"Aprovação: {int(percentAprovavao)}%")

inputDados = input("")

correcaoProvas(inputDados)