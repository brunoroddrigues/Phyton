# Solicita ao usuário que insira uma frase
frase = input("Digite uma frase: ")

# Conta o número de palavras
contagem_palavras = len(frase.split())

# Exibe o resultado
print(f"A frase contém {contagem_palavras} palavras.")

input("Pressione Enter para sair...")
