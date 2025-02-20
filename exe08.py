#8-	Defina uma variável chamada total peça ao usuário para inserir cinco números e após cada entrada pergunte se ele deseja que esse numero seja incluído ( S ou s ) , ( N ou n) ,
#  se ele desejar adicione o numero ao total. Se ele não quiser inclui-lo não adicione ao local, depois de exibir os cinco números exiba o total
total = []
num1 = int(input("Digite o primeiro número : "))
num2 = int(input("Digite o segundo número : "))
num3 = int(input("Digite o terceiro número : "))
num4 = int(input("Digite o quarto número : "))             
num5 = int(input("Digite o quinto número : "))
resposta1 = input("Deseja incluir o primeiro número ? s/n ")
resposta2 = input("Deseja incluir o segundo número ? s/n ")
resposta3 = input("Deseja incluir o terceiro número ? s/n ")
resposta4 = input("Deseja incluir o quarto número ? s/n ")
resposta5 = input("Deseja incluir o quinto número ? s/n ")
if resposta1 == 's' or 'S':
    total.append(num1)

elif resposta2 == 's' or 'S':
    total.append(num2)
       
elif resposta3 == 's' or 'S':
    total.append(num3)

elif resposta4 == 's' or 'S':
    total.append(num4)

elif resposta5 == 's' or 'S':
    total.append(num5)
    print(total)
    print("Mateus De Campos Turkoco")
