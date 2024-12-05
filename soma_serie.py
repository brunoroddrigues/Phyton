# Solicita ao usuário que insira o número de termos da série
n = int(input("Digite o número de termos da série: "))

# Inicializa o somatório
soma = 0

# Calcula o somatório
for i in range(1, n + 1):
    soma += 1 / i

# Exibe o resultado
print(f"O somatório da série é: {soma:.2f}")

input("Pressione Enter para sair...")
