import math

# Solicita ao usuário que insira o raio do círculo
raio = float(input("Digite o raio do círculo: "))

# Calcula a área do círculo
area = math.pi * (raio ** 2)

# Exibe o resultado
print(f"A área do círculo é: {area:.2f}")

input("Pressione Enter para sair...")
