# Solicita uma string e um número inteiro como entrada, depois retorna a string repetida o número de vezes informado

# Captura a string
nome = input("Digite uma string: ")

# Captura o valor numérico
try:
    valor = int(input("Digite um valor: "))
    
    # Verifica se o valor é válido
    if valor <= 0:
        print("Por favor, insira um número válido maior que zero.")
    else:
        # Cria a string repetida com espaços
        print(" ".join([nome] * valor))
except ValueError:
    print("Por favor, insira um número inteiro válido.")
