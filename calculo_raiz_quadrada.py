import math

# Solicita ao usuário que insira um número não negativo
numero = float(input("Digite um número não negativo: "))

# Calcula a raiz quadrada
if numero < 0:
    print("Erro: Não é possível calcular a raiz quadrada de um número negativo.")
else:
    raiz_quadrada = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} é: {raiz_quadrada:.2f}")

input("Pressione Enter para sair...")
