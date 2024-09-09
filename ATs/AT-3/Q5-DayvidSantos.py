valorPago = float(input('Informe o valor: '))
codigo = int(input('Informe o codigo: '))



match codigo:
    case 1:
        novoValor = valorPago-(valorPago*0.30)
        print(f'{codigo} x de R$ {novoValor}')
    case 2:
        novoValor = valorPago-(valorPago*0.20)
        parcela = novoValor/codigo
        print(f'{codigo} x de R$ {parcela}')
    case 3:
        novoValor = valorPago-(valorPago*0.10)
        parcela = novoValor/codigo
        print(f'{codigo} x de R$ {parcela}')
    case 4:
        parcela = valorPago/codigo
        print(f'{codigo} x de R$ {parcela}')
    case _:
        print( 'ERROR')



