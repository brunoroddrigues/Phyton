# Solicita ao usuário que insira um número
n = int(input("Digite o número de termos da sequência de Fibonacci que deseja: "))

# Inicializa os primeiros termos
a, b = 0, 1

# Exibe a sequência de Fibonacci
print("Sequência de Fibonacci:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

print()  # Pula para a próxima linha
input("Pressione Enter para sair...")
