# Solicita ao usuário que insira números separados por espaço
numeros = input("Digite vários números separados por espaço: ")

# Converte a entrada em uma lista de inteiros
lista_numeros = [int(num) for num in numeros.split()]

# Encontra o maior e o menor número
maior = max(lista_numeros)
menor = min(lista_numeros)

# Exibe o resultado
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")

input("Pressione Enter para sair...")
