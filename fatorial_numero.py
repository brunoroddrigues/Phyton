# Solicita ao usuário que insira um número
numero = int(input("Digite um número inteiro não negativo: "))

# Inicializa o fatorial
fatorial = 1

# Calcula o fatorial do número
for i in range(1, numero + 1):
    fatorial *= i

# Exibe o resultado
print(f"O fatorial de {numero} é: {fatorial}")

input("Pressione Enter para sair...")
