# Solicita ao usuário que insira a temperatura em Celsius
celsius = float(input("Digite a temperatura em Celsius: "))

# Converte Celsius para Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Exibe o resultado
print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}")

input("Pressione Enter para sair...")
