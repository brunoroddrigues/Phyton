import math

# Solicita ao usuário que insira as coordenadas dos pontos
x1, y1 = map(float, input("Digite as coordenadas do primeiro ponto (x1 y1): ").split())
x2, y2 = map(float, input("Digite as coordenadas do segundo ponto (x2 y2): ").split())

# Calcula a distância
distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Exibe o resultado
print(f"A distância entre os pontos é: {distancia:.2f}")

input("Pressione Enter para sair...")
