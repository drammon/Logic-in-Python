def calcSoma(N):
    soma = 0
    for i in range(1, (N+1)):
        soma += i
    return soma

num = int(input())
print(calcSoma(num))