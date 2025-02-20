#4-	Escreva um programa para pedir um numero e em seguida o nome, exiba o nome (uma letra de cada vez em cada linha ) e repita isso para o numero de vezes que ele digitou
numero = int(input("Digite um numero: "))
nome = input("Qual seu nome: ")
for i in range(numero):
    for letras in nome:
        print(letras)