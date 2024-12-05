# Solicita ao usuário que insira a renda
renda = float(input("Digite a sua renda anual: "))

# Calcula o imposto de renda
if renda <= 22847.76:
    imposto = 0
elif renda <= 33919.80:
    imposto = (renda - 22847.76) * 0.15
else:
    imposto = (renda - 33919.80) * 0.275 + (11072.04 * 0.15)

# Exibe o resultado
print(f"O imposto de renda a ser pago é: R$ {imposto:.2f}")

input("Pressione Enter para sair...")
