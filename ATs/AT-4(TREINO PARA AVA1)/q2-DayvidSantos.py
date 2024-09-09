vitorias = 0
count = 0
while True:
    
    if count < 6:
        result = input().lower()
        if result == "v":
            vitorias += 1
            count += 1
            print(count)
            print(vitorias)
        elif result == "p":
            count += 1
        else:
            break
    else:
        match vitorias:
            case 0:
                print("-1")
            case 1:
                print("3")
            case 2:
                print("3")
            case 3:
                print("2")
            case 4:
                print("2")
            case 5:
                print("1")
            case 6:
                print("1")
        break






