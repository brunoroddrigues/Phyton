# Função para calcular o Máximo Divisor Comum (MDC)
def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

# Solicita ao usuário que insira dois números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Calcula o MMC
mmc = abs(num1 * num2) // mdc(num1, num2)

# Exibe o resultado
print(f"O Mínimo Múltiplo Comum (MMC) de {num1} e {num2} é: {mmc}")

input("Pressione Enter para sair...")
