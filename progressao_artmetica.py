# Solicita ao usuário que insira o primeiro termo e a razão da PA
primeiro_termo = float(input("Digite o primeiro termo da PA: "))
razao = float(input("Digite a razão da PA: "))

# Solicita o número de termos
n = int(input("Digite o número de termos da PA: "))

# Exibe os termos da PA
print("Os termos da PA são:")
for i in range(n):
    termo = primeiro_termo + i * razao
    print(termo, end=" ")

print()  # Pula para a próxima linha
input("Pressione Enter para sair...")
