# Solicita ao usuário que insira as notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média
media = (nota1 + nota2 + nota3) / 3

# Exibe a média
print(f"A média do aluno é: {media:.2f}")

# Verifica se o aluno foi aprovado ou reprovado
if media >= 6.0:
    print("Aluno Aprovado!")
else:
    print("Aluno Reprovado!")

input("Pressione Enter para sair...")
