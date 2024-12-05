def soma_pares(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    return soma

# Solicita ao usuário para inserir uma lista de números
entrada = input("Digite varios numeros ")
numeros = list(map(int, entrada.split()))

resultado = soma_pares(numeros)
print(f"A soma dos números pares é: {resultado}")
input("Pressione Enter para sair...")
