# Solicita ao usuário que insira duas palavras
palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

# Verifica se as palavras são anagramas
if sorted(palavra1) == sorted(palavra2):
    print(f"{palavra1} e {palavra2} são anagramas.")
else:
    print(f"{palavra1} e {palavra2} não são anagramas.")

input("Pressione Enter para sair...")
