# Solicita ao usuário que insira uma frase
frase = input("Digite uma frase: ")

# Conta as vogais
vogais = "aeiouAEIOU"
contagem_vogais = sum(1 for letra in frase if letra in vogais)

# Exibe o resultado
print(f"A contagem de vogais na frase é: {contagem_vogais}")

input("Pressione Enter para sair...")
