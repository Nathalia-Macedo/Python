# Exercícios Propostos

# Exercício 1: Peça ao usuário uma idade e determine se a pessoa é maior ou menor de idade.

idade = int(input("Digite a sua idade: "))
if(idade>=18):
    print(" Você é maior de idade!")
else: 
    print("Você é menor de idade!")
    

# Exercício 2: Solicite um número e determine se ele é par ou ímpar.

numero = int(input("Digite um número: "))
if(numero%2==0):
    print(f" O número {numero} é par")
else:
    print(f"O número {numero} é ímpar!")

# Exercício 3: Solicite uma temperatura e determine se está quente (acima de 30°C), agradável (entre 20°C e 30°C) ou frio (abaixo de 20°C).

temperatura = float(input("Digite uma temperatura: "))
if(temperatura<20):
    print("Frio")
elif(temperatura>20 and temperatura<=30):
    print("Agradável")
else:
    print("Quente")

# Exercício 4: Solicite um número e verifique se ele é positivo, negativo ou zero.

num = int(input("Digite um número:"))
if(num>0):
    print("Positivo")
elif(num<0):
    print("Negativo")
else:
    print(" O número é 0")

# Exercício 5: Solicite um número e verifique se ele está no intervalo de 10 a 50.

num1 = int(input("Digite um número entre 1 e 50:"))
if num1>=1 and num1<=50:
    print(f" O número {num1} está entre 1 e 50")
else:
    print(f' O número {num1} não está no intervalo solicitado')

# Exercício 6: Peça ao usuário um número de 1 a 7 e exiba o dia da semana correspondente.

numero_da_semana = int(input("Digite um número de 1 a 7: "))
if numero_da_semana==1:
    print(f"Segunda Feira")
elif numero_da_semana==2:
    print("Terça-feira")
elif numero_da_semana==3:
    print("Quarta-Feira")
elif numero_da_semana==4:
    print("Quinta-feira")
elif numero_da_semana==5:
    print("Sexta-feira")
elif numero_da_semana==6:
    print("sábado")
else:
    print("Domingo")

# Exercício 7: Solicite uma idade e uma altura, e determine se a pessoa pode participar de um brinquedo em um parque de diversões (idade > 12 e altura > 1,40 m).

idade = int(input("Digite a idade: "))
altura = float(input("Digite a altura: "))
if idade>12 and altura>1.40:
    print("Você pode brincar!")
else:
    print("Você não pode brincar!")

# Exercício 8: Solicite dois números e determine o maior deles.

number1 = int(input("DIgite um número: "))
number2 = int(input("Digite mais um número: "))
if(number1>number2):
    print(" O primeiro número digitado é o maior.")
elif number2>number1:
    print("O segundo número digitado é o maior")
else: 
    print("Os números são iguais!")

# Exercício 9: Solicite três números e determine o menor deles.

num_a = int(input("Digite um número: "))
num_b = int(input("Digite outro número: "))
num_c = int(input("Digite o último número: "))
if(num_a>num_b and num_a>num_c):
    print(f"O maior número é o {num_a}")
elif(num_b > num_a and num_b >num_c):
    print(f"O maior número é o {num_b}")
else:
    print(f"O maior número é o {num_c}")

# Exercícios 10: Solicite três números e determine se eles podem formar um triângulo (soma de dois lados é maior que o terceiro).

primeiro_lado = int(input("Digite um número: "))
segundo_lado = int(input("Digite um segundo número: "))
terceiro_lado = int(input("Digite o ultimo número: "))
if(primeiro_lado+segundo_lado>terceiro_lado):
    print("Formam um triângulo")
else:
    print("Não formam um triângulo")
    

# Exercício 11: Crie um programa que verifica se um número está fora do intervalo de 50 a 100.

n = int(input("Digite um número: "))
if(n>=50 and n<=100):
    print(f"{n} está no intervalo de 50 a 100")
else:
    print(f"{n} não está no intervalo de 50 a 100")

# Exercício 12: Faça um programa que verifica se um número é igual a 7 ou 8.

x = int(input("Digite um número: "))
if(x==7 or x==8):
    print("O número é igual a 7 ou a 8")
else:
    print(" O número não é nem 7 nem 8")
    

# Exercício 13:Escreva um programa que verifica se um número é diferente de 0.

numero_do_usuario = int(input("DIgite um número: "))
if(numero_do_usuario>0 or numero_do_usuario<0):
    print(" O número é diferente de 0")
else:
    print(" O número é igual a 0")

# Exercícios 14: Crie um programa que verifica se um número é maior do que 5 e menor do que 15.

x = int(input("Digite um número:"))
if x>5 and x <15:
    print(f" O número {x} é maior do que 5 e menor do que 15")

# Exercício 15: Faça um programa que verifica se um número é maior do que 100 ou menor do que -100.

n = int(input("DIgite um número: "))
if n>100:
    print(" O número é maior do que 100")
elif n<-100:
    print(" O número é menor do que -100")