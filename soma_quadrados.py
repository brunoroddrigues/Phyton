# Solicita ao usuário que insira um número
n = int(input("Digite um número inteiro positivo: "))

# Calcula a soma dos quadrados de 1 a n
soma_quadrados = sum(i ** 2 for i in range(1, n + 1))

# Exibe o resultado
print(f"A soma dos quadrados de 1 a {n} é: {soma_quadrados}")

input("Pressione Enter para sair...")
