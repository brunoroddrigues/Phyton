# Solicita ao usuário que insira um número
n = int(input("Digite um número inteiro positivo: "))

# Gera um dicionário com números e seus quadrados
quadrados = {i: i**2 for i in range(1, n + 1)}

# Exibe o dicionário
print("Dicionário de números e seus quadrados:")
for numero, quadrado in quadrados.items():
    print(f"{numero}: {quadrado}")

input("Pressione Enter para sair...")
