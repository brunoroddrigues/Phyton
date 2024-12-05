# Solicita ao usuário que insira um número
numero = int(input("Digite um número inteiro: "))

# Gera e exibe a tabela de multiplicação
print(f"Tabela de multiplicação do {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

input("Pressione Enter para sair...")
