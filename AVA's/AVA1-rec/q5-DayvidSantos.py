quota = int(input())

n = int(input())

resto = 0
for i in range (1, n + 1):
    q = int(input())
    if q > quota:
        resto += quota - q
    if q < quota:
        resto += quota - q

print(quota + resto)