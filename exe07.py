#7-	Peça ao usuário para inserir seu nome e um numero. Se o numero for menor que 10 exiba o nome dele esse numero de vezes caso contrario exiba a mensagem “numero muito alto” três vezes
nome = input("Digite seu nome : ")
num = int(input("Digite um número inteiro : "))
if num < 10:
    for i in range(num):
        print(nome)
        print("Mateus De Campos Turkoco")
else:
    for i in range(3):
        print("Numero muito alto")        
