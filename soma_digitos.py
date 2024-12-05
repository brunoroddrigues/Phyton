# Solicita ao usuário que insira um número
numero = input("Digite um número inteiro: ")

# Calcula a soma dos dígitos
soma_digitos = sum(int(digito) for digito in numero)

# Exibe o resultado
print(f"A soma dos dígitos do número {numero} é: {soma_digitos}")

input("Pressione Enter para sair...")
