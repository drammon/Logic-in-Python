num = int(input())

count = 0
for i in range(1, (num//2)+1):
    if num % i == 0: 
        count += 1
print(count + 1)