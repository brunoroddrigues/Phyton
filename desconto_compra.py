# Solicita ao usuário que insira o valor da compra e o percentual de desconto
valor_compra = float(input("Digite o valor da compra: "))
desconto = float(input("Digite o percentual de desconto: "))

# Calcula o valor com desconto
valor_final = valor_compra * (1 - desconto / 100)

# Exibe o resultado
print(f"O valor final após o desconto é: {valor_final:.2f}")

input("Pressione Enter para sair...")
