#2-	Faça um programa que solicite ao usuário para digitar seu nome e um numero qualquer e em seguida exiba seu nome varias vezes de acordo com numero que ele digitou
nome = input("Digite seu nome : ")
num = int(input("Digite um número inteiro : "))
for i in range(num):
    print(nome)