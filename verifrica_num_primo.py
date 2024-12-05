# Solicita ao usuário que insira um número
numero = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é primo
if numero < 2:
    print(f"{numero} não é um número primo.")
else:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            print(f"{numero} não é um número primo.")
            break
    else:
        print(f"{numero} é um número primo.")

input("Pressione Enter para sair...")
