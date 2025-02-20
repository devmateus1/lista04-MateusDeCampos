#9-	Faça um programa que pergunte em qual direção deseja apontar ,
#  se ele selecionar para cima, peça um numero superior e conta de um ate esse numero, item 2 ,
#  se ele selecionar para baixo, peça lhe para inserir um numero abaixo de 20 e em seguida faça a contagem regressiva de 20 até esse numero, 
direcao = (input("A que direção você quer apontar cima/baixo) :  "))
if direcao == 'cima':
    num1 = int(input("Digite um número : "))
    for i in range(num1 + 1):
        print(i)
elif direcao == 'baixo':
    num2 = int(input("Digite um número abaixo de 20: "))
    for j in range(num2 + 1):
        print(j) 
else:
    print("Número inválido")               