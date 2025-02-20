#4-	Escreva um programa para pedir um numero e em seguida o nome, exiba o nome (uma letra de cada vez em cada linha ) e repita isso para o numero de vezes que ele digitou
num = int(input("Digite um número inteiro : "))
nome = input("Digite seu nome : ")
for letra in nome:
    print(letra in range(num))