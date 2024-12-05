import random

# Gera um número aleatório entre 1 e 50
numero_secreto = random.randint(1, 50)
tentativas = 0

print("Bem-vindo ao jogo 'Adivinhe o Número'!")
print("Estou pensando em um número entre 1 e 50.")

while True:
    palpite = int(input("Qual é o seu palpite? "))
    tentativas += 1

    if palpite < numero_secreto:
        print("Muito baixo! Tente novamente.")
    elif palpite > numero_secreto:
        print("Muito alto! Tente novamente.")
    else:
        print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativas} tentativas.")
        break

input("Pressione Enter para sair...")
