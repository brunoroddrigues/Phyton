# Solicita ao usuário que insira uma frase
frase = input("Digite uma frase: ")

# Inicializa a contagem de vogais
contagem_vogais = 0

# Define as vogais
vogais = "aeiouAEIOU"

# Conta as vogais na frase
for letra in frase:
    if letra in vogais:
        contagem_vogais += 1

# Exibe o resultado
print(f"A frase contém {contagem_vogais} vogais.")

input("Pressione Enter para sair...")
