import math

X1=float(input("Para calcular o valor da distância entre dois pontos num plano cartesiano, defina o valor de X1: "))
Y1=float(input("Defina o valor de Y1: "))
X2=float(input("Defina o valor de X2: "))
Y2=float(input("Defina o valor de Y2: "))

calcX= (X2-X1)**2
calcY= (Y2-Y1)**2
dist = math.sqrt(calcX+calcY)
print("asasasa", dist)

print(f"A distância entre os pontos é de: {dist:.4f}")
