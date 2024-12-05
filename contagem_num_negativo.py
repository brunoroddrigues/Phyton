# Solicita ao usuário que insira números separados por espaço
numeros = input("Digite vários números separados por espaço: ")

# Converte a entrada em uma lista de inteiros
lista_numeros = [int(num) for num in numeros.split()]

# Conta os números negativos
contagem_negativos = sum(1 for num in lista_numeros if num < 0)

# Exibe o resultado
print(f"A quantidade de números negativos é: {contagem_negativos}")

input("Pressione Enter para sair...")
