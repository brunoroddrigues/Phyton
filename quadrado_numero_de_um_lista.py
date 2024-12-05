# Solicita ao usuário que insira números separados por espaço
numeros = input("Digite vários números separados por espaço: ")

# Converte a entrada em uma lista de inteiros
lista_numeros = [int(num) for num in numeros.split()]

# Calcula o quadrado de cada número
quadrados = [num ** 2 for num in lista_numeros]

# Exibe o resultado
print("Os quadrados dos números são:", quadrados)

input("Pressione Enter para sair...")
