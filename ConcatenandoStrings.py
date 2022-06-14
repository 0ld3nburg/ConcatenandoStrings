#Entrada de dados

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
ru = int(input("Digite seu RU: "))

#Convertendo ru em string

n = str(ru)

#Concatendando os dados com .lower() para manter as letras minusculas

email = nome.lower()[0] + sobrenome.lower()[:] + n[-2:] + "@algoritmos.com.br"

#Saida de dados

print(f"O Sr(a) {nome} {sobrenome}, seu email é: {email}")