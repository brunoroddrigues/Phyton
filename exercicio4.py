numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (soma, subtração, multiplicação, divisão): ").lower()

if operacao == "soma":
    resultado = numero1 + numero2
elif operacao == "subtração":
    resultado = numero1 - numero2
elif operacao == "multiplicação":
    resultado = numero1 * numero2
elif operacao == "divisão":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Erro! Divisão por zero não é permitida."
else:
    resultado = "Operação inválida!"

print(f"O resultado da operação é: {resultado}")
input("Pressione Enter para sair...")
