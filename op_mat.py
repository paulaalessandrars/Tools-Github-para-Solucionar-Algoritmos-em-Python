# Vamos solicitar como entrada dois números e depois realizar uma operação entre eles

# Captura os valores e converte para números
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

# Captura a operação desejada
operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")

# Verifica a operação e realiza o cálculo
if operacao == "+":
    print("Resultado:", valor1 + valor2)
elif operacao == "-":
    print("Resultado:", valor1 - valor2)
elif operacao == "*":
    print("Resultado:", valor1 * valor2)
elif operacao == "/":
    if valor2 == 0:
        print("Erro: divisão por zero não é permitida.")
    else:
        print("Resultado:", valor1 / valor2)
else:
    print("Operação inválida.")
