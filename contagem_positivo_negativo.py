# Solicita ao usuário que insira números separados por espaço
numeros = input("Digite vários números separados por espaço: ")

# Converte a entrada em uma lista de floats
lista_numeros = [float(num) for num in numeros.split()]

# Conta positivos e negativos
positivos = sum(1 for num in lista_numeros if num > 0)
negativos = sum(1 for num in lista_numeros if num < 0)

# Exibe o resultado
print(f"Números positivos: {positivos}, Números negativos: {negativos}")

input("Pressione Enter para sair...")
