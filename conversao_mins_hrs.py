# Solicita ao usuário que insira o tempo em minutos
minutos = int(input("Digite o tempo em minutos: "))

# Calcula horas e minutos
horas = minutos // 60
minutos_restantes = minutos % 60

# Exibe o resultado
print(f"{minutos} minutos equivalem a {horas} horas e {minutos_restantes} minutos.")

input("Pressione Enter para sair...")
