# Solicita ao usuário que insira o preço do produto
preco = float(input("Digite o preço do produto: "))

# Aplica desconto progressivo baseado no preço
if preco < 100:
    desconto = 5  # 5%
elif 100 <= preco < 200:
    desconto = 10  # 10%
else:
    desconto = 15  # 15%

# Calcula o preço final
preco_final = preco - (preco * (desconto / 100))

# Exibe o resultado
print(f"O preço final após um desconto de {desconto}% é: {preco_final:.2f}")

input("Pressione Enter para sair...")
