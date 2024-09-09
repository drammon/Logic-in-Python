def valida_string(palavra, min, max):
    return min <= len(palavra) <= max

entrada = input("")

partes = entrada.split(',')

string = partes[0].strip()  
min_len = int(partes[1].strip())  
max_len = int(partes[2].strip())


resultado = valida_string(string, min_len, max_len)

print(resultado)