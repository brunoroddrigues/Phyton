# Solicita ao usuário que insira uma palavra ou frase
texto = input("Digite uma palavra ou frase: ")

# Remove espaços e converte para minúsculas
texto_limpo = ''.join(texto.split()).lower()

# Verifica se é um palíndromo
if texto_limpo == texto_limpo[::-1]:
    print(f"'{texto}' é um palíndromo.")
else:
    print(f"'{texto}' não é um palíndromo.")

input("Pressione Enter para sair...")
