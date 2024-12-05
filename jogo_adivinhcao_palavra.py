import random

# Lista de palavras
palavras = ["python", "programacao", "computador", "desenvolvimento", "algoritmo"]
palavra_secreta = random.choice(palavras)
tentativas = 6

print("Bem-vindo ao jogo de adivinhação de palavras!")
print("Você tem 6 tentativas para adivinhar a palavra.")

while tentativas > 0:
    palpite = input("Digite uma letra: ").lower()

    if palpite in palavra_secreta:
        print(f"Boa! A letra '{palpite}' está na palavra.")
    else:
        tentativas -= 1
        print(f"Ops! A letra '{palpite}' não está na palavra. Você ainda tem {tentativas} tentativas.")

    # Verifica se o jogador adivinhou a palavra
    if all(letra in palpite for letra in palavra_secreta):
        print(f"Parabéns! Você adivinhou a palavra: {palavra_secreta}.")
        break
else:
    print(f"Você não conseguiu adivinhar a palavra. Ela era: {palavra_secreta}.")

input("Pressione Enter para sair...")
