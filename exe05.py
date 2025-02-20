#5-	Peça ao usuário para inserir um numero que deseja a tabuada e em seguida exibir a tabuada para este numero
num = int(input("Digite um número inteiro : "))
for i in range(11):
    tabuada = num * i
    print(num ,"x",i,"=", tabuada)