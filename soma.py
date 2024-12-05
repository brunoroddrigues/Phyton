#1. Cálculo da soma de números inteiros até um número fornecido pelo usuário

# Solicita ao usuário que insira um número
numero = int(input("Digite um número inteiro positivo: "))

# Inicializa a soma
soma = 0

# Calcula a soma de todos os números inteiros de 1 até o número fornecido
for i in range(1, numero + 1):
    soma += i

# Exibe o resultado
print(f"A soma dos números de 1 a {numero} é: {soma}")

input("Pressione Enter para sair...")
