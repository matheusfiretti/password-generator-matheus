import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
letras_senha = int(input('Digite a quantidade de letras que deseja na sua senha:\n'))
numeros_senha = int(input('Digite a quantidade de numeros que deseja na sua senha:\n'))
simbolos_senha = int(input('Digite a quantidade de simbolos que deseja na sua senha:\n'))
n_caracteres = letras_senha + numeros_senha + simbolos_senha

senha_lista = []

for i in range(letras_senha):
    senha_lista.append(random.choice(letras))

for i in range(numeros_senha):
    senha_lista.append(random.choice(numeros))

for i in range(simbolos_senha):
    senha_lista.append(random.choice(simbolos))

random.shuffle(senha_lista)

senha = ''
for i in range(n_caracteres):
    senha += senha_lista[i]

print(f'Sua senha é: {senha}')