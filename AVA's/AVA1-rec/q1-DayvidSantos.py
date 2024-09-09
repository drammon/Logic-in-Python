cod = int(input())

match cod:
    case 1:
        print("SUL")
    case 2:
        print("NORTE")
    case 3:
        print("LESTE")
    case 4:
        print("OESTE")
    
if cod == 5 or cod == 6 or (cod > 20 and cod < 31) :
    print ("NORDESTE")
elif cod > 6 and cod < 10:
    print("SUDESTE")
elif cod > 9 and cod < 21:
    print("CENTRO-OESTE")