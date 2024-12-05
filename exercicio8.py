import random

numero_secreto = random.randint(1, 100)  # Gera um número secreto entre 1 e 100
tentativas = 0

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número secreto entre 1 e 100.")

while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite < numero_secreto:
        print("Muito baixo! Tente novamente.")
    elif palpite > numero_secreto:
        print("Muito alto! Tente novamente.")
    else:
        print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativas} tentativas.")
        break

input("Pressione Enter para sair...")
