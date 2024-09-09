
num1 = int(input())
num2 = int(input())

if num1 > num2:
    if num1 % num2 == 0:
        print("Sim")
    else:
        print("Não")
else: 
    if num2 % num1 == 0:
        print("Sim")
    else:
        print("Não")

