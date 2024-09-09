ageDog = int(input())
ageHuman = 0

if ageDog >= 0 and ageDog <= 2:
    ageHuman = ageDog * 21
elif ageDog > 2 and ageDog <= 4:
    ageHuman = 42 + (ageDog - 2) * 5
elif ageDog > 4 and ageDog <= 7:
    ageHuman = 52 + (ageDog - 4) * 3
else:
    ageHuman = 61 + (ageDog - 7) * 2

print(int(ageHuman))

