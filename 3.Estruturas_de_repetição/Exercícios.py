#Exercícios Propostos
'''
Exercício 1: Adivinhe o número: Crie um jogo em que o programa
# gera um número aleatório e o jogador precisa adivinhar qual é.
# Use um laço "while" para permitir várias tentativas.
# Utilize a palavra-chave "break" quando o jogador acertar.

# '''
# import random
# #A biblioteca random vai gerar um numero aleatório entre 1 e 20.
# # Essa linha de código fica fora do laço por que, se estivesse dentro do loop,
# # a cada iteração, seria gerado um número diferente
# numero_aleatorio = random.randint(1,21)
# #definindo quantas tentativas o usuário pode ter
# tentativas = 5
# ganhou = False
# #enquanto tentativas for maior do que 0, o usuário pode continuar tentando:
# while tentativas>0:
#     numero_palpite = int(input("Digite o seu palpite: "))
#     if numero_palpite > numero_aleatorio:
#         tentativas-=1
#         print(f" O número que estamos procurando é menor do que {numero_palpite}. Tentativas: {tentativas}")
#     elif numero_palpite < numero_aleatorio:
#         tentativas-=1
#         print(f" O número que estamos procurando é maior do que {numero_palpite}. Tentativas: {tentativas}")
#     else:
#         tentativas-=1
#         print(f"Parabéns! Você acertou depois de {5-tentativas} tentativas")
#         ganhou=True
#         break
# if tentativas==0 and ganhou==False:
#         print("Que pena, você não acertou o número aleatório!")
        
'''
Exercício 2: Tabuada interativa: Peça ao usuário para digitar um número e mostre a tabuada desse número. Use um laço "while" para continuar perguntando ao usuário por mais números até que ele digite zero.

'''

# while True:
#     numero = int(input("Digite o número que ela gostaria de ver a tabuada: "))
#     if numero==0:
#         break
#     for i in range(0,11):
#         print(f"{numero} X {i} = {numero*i}")

'''
Exercício 3:Escreva um programa que imprima os números de 1 a 10.
'''

# for i in range(1,11,1):
#     print(i)

'''
Exercício 4:Imprima os números pares de 1 a 20.
'''

# for i in range(0,21,2):
#     print(i)

'''
Exercício 5:Calcule a soma dos números de 1 a 50.

'''
# soma = 0

# for i in range(1,51):
#     soma+=i
# print(soma)   

'''
Exercício 6:Faça um programa que imprima a tabuada do 7.

'''

# for i in range(1,10,1):
#     print(f"7 X {i} = {7*i}")

'''
Exercício 7:Imprima os números de 10 a 1 em ordem decrescente.

'''

# for i in range(10,0,-1):
#     print(i)

'''
Exercícios 8: Escreva um programa que imprima os caracteres de uma string.

'''

# string = "PALAVRA"

# for letra in string:
#     print(letra)

'''
Exercício 9: Imprima os números de 0 a 100 de 10 em 10.
'''

# for i in range(0,101,10):
#     print(i)
    
    
'''
Exercício 10:Calcule a média de cinco números fornecidos pelo usuário.

'''
# soma = 0
# media = 0
# for i in range(1,6):
#     numero = int(input(f"Digite o numero {i}"))
#     soma+=numero
# media = soma/5
# print(media)

'''
Exercício 11:Imprima os números ímpares de 1 a 100.

'''
# for i in range(-1,101,2):
#     print(i)    

'''
Exercícios 12: Conte e imprima os números pares de 1 a 20 usando um loop while.

'''
# valor = 1

# while valor < 21:
#     print(valor)
#     valor+=1

'''
Exercício 13:Calcule a soma dos números de 1 a 50 usando um loop while.

'''

# numero = 1
# soma = 0
# while numero<51:
#     soma+=numero
#     numero+=1
# print(soma)

'''
Exercício 14: Escreva um programa que imprima os números de 10 a 1 em ordem decrescente usando um loop while.

'''

# numero = 10

# while numero>0:
#     print(numero)
#     numero-=1

'''
Exercício 15:Imprima os números primos de 1 a 50 usando um loop while.
'''
# Inicializa o contador
# numero = 1

# # Loop while para percorrer os números de 1 a 50
# while numero <= 50:
#     # Verifica se o número atual é primo
#     if numero > 1:
#         # Verifica se há algum divisor entre 2 e a raiz quadrada do número
#         for i in range(2, int(numero**0.5) + 1):
#             if numero % i == 0:
#                 break  # O número não é primo, interrompe o loop
#         else:
#             # Se nenhum divisor foi encontrado, o número é primo e é impresso
#             print(numero, end=' ')
    
#     # Incrementa o contador para verificar o próximo número
#     numero += 1

# # Quebra de linha no final para melhor formatação
# print()

'''
Exercício 16:Imprima os números ímpares de 1 a 100.

'''

# for i in range(1,101,2):
#     print(i) 

'''
Exercícios 17: Imprima os números ímpares de 1 a 100 usando um loop while.

'''


# valor = 1
# while valor <101:
#     if valor%2!=0:
#         print(valor)
#         valor+=1
#     valor+=1


