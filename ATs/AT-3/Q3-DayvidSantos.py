codigo = int (input("Digite o codigo: "))
quantidade = float (input ("Digite a quantidade em kg: "))

match codigo:
    case 1: 
        if quantidade <=5:
           x= quantidade*7
           print(f"o valor total é {x}")
        else:
            x=quantidade*5.80
            print(f"o valor total é {x}")
    case 2:
        if quantidade <=5:
            x= quantidade * 11.80
            print(f"o valor total é {x}")
        else:
            x= quantidade*8.50
            print(f"o valor total é {x}")
    case 3:
        if quantidade <=5:
           x= quantidade*11.80
           print(f"o valor total é {x}")
        else:
            x=quantidade*8.50
            print(f"o valor total é {x}")
    case 4:
        if quantidade <=5:
           x= quantidade*2.25
           print(f"o valor total é {x}")
        else:
            x=quantidade*1.70
            print(f"o valor total é {x}")
    case 5:
        if quantidade <=5:
           x= quantidade*6.90
           print(f"o valor total é {x}")
        else:
            x=quantidade*5.50
            print(f"o valor total é {x}")
    case 6:
        if quantidade <=5:
           x= quantidade*4.50
           print(f"o valor total é {x}")
        else:
            x=quantidade*2.40
            print(f"o valor total é {x}")
    case _:
        print ("Número invalido!")
    

                   
                   