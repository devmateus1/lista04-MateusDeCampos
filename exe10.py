#- Faça um programa que pergunte quantas pessoas o usuário deseja convidar para uma festa.
#	Se ele digitar um número abaixo de 10, peça os nomes e após cada nome exiba a mensagem: "[nome] está convidado para a festa". 
#	Se ele inserir um número 10 ou superior, exiba a mensagem "Muitas pessoas".
convidados = int(input("Quantos convidados você queira desejar : "))
if convidados <= 10: 
    for pessoa in range(convidados):
        nomes = input("Qual nome do convidado: ")
        print(nomes, 'foi convidado para a festa')
elif convidados > 10:
    print("Muitas pessoas")        
