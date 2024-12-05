# Solicita ao usuário que insira o número de notas
n = int(input("Digite o número de notas: "))

# Inicializa a soma das notas
soma_notas = 0

# Loop para coletar as notas
for i in range(n):
    nota = float(input(f"Digite a nota {i + 1}: "))
    soma_notas += nota

# Calcula a média
media = soma_notas / n

# Exibe a média e a situação do aluno
print(f"A média das notas é: {media:.2f}")
if media >= 6.0:
    print("Aluno Aprovado!")
else:
    print("Aluno Reprovado!")

input("Pressione Enter para sair...")
