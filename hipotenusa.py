import math

# Solicita ao usuário que insira os catetos do triângulo retângulo
cateto1 = float(input("Digite o comprimento do primeiro cateto: "))
cateto2 = float(input("Digite o comprimento do segundo cateto: "))

# Calcula a hipotenusa
hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

# Exibe o resultado
print(f"A hipotenusa do triângulo retângulo é: {hipotenusa:.2f}")

input("Pressione Enter para sair...")
