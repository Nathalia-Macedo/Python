#Exercícios propostos

#Exercício 1: Crie um programa que exiba "Olá, mundo!" na tela.

print("Olá mundo")

#Exercício 2: Peça ao usuário que insira seu nome e, em seguida, exiba uma saudação com o nome.

nome_do_usuario = str(input("Digite o seu nome: "))
print(f'Seja bem vindo {nome_do_usuario}')

#Exercício 3: Solicite dois números ao usuário e calcule a soma.

primeiro_numero = int(input("Digite um número: "))
segundo_numero = int(input("Digite mais um número: "))
soma = primeiro_numero+segundo_numero
print(soma)

#Exercício 4: Peça ao usuário um número e exiba o dobro desse número.

numero = int(input("Digite um número: "))
dobro = numero*2
print(f' O dobro de {numero} é {dobro}')

#Exercício 5: Solicite a largura e a altura de um retângulo e calcule a área.

altura = float(input("Digite a altura: "))
largura = float(input("Digite a largura: "))
area = altura*largura
print(f"A área do retângulo é de {area}")

#Exercício 6: Solicite o raio de um círculo e calcule a área da circunferência.

raio = int(input("Digite o raio do círculo: "))
pi = 3.14
area_da_circunferencia = pi*raio
print(f" a área da circunferência é de {area_da_circunferencia}")

#Exercício 7: Peça um valor em dólares e converta-o para reais (considere uma taxa de câmbio fixa).

valor_em_dolares = float(input("Digite um valor em dólares: "))
taxa_de_cambio = 5
valor_convertido = valor_em_dolares/taxa_de_cambio
print(f"{valor_em_dolares} dolares equivale a {valor_convertido} reais")

#Exercício 8: Solicite a temperatura em graus Celsius e converta-a para graus Fahrenheit.

temperatura_celsius = float(input("Digite a temperatura em graus celsius: "))
fahrenheit = (temperatura_celsius*9/5)+32
print(f"{temperatura_celsius} celsius em fahrenheit equivale a {fahrenheit}")

#Exercício 9: Solicite o nome, idade e cidade do usuário e exiba essas informações em uma única linha.

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
cidade = str(input("Digite o nome da sua cidade: "))
print(f" O seu nome é {nome}, você tem {idade} anos e mora em {cidade}")

#Exercício 10: Solicite o peso e a altura do usuário e calcule o IMC (Índice de Massa Corporal).

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
IMC = peso*(altura**2)
print(f"Seu IMC é de {IMC}")

#Exercício 11: Solicite um número e calcule a raiz quadrada.

numero_do_usuario = int(input("Digite o número que gostaria de saber a raiz quadrada: "))
raiz_quadrada = numero_do_usuario**2
print(f'A raiz quadrada de {numero_do_usuario} equivale a {raiz_quadrada}')

#Exercício 12: Solicite a quantidade de maçãs e peras e calcule o custo total (maçãs a R$ 0,30 cada e peras a R$ 0,25 cada).

quantidade_macas = int(input("Digite a quantidade de maçãs: "))
quantidade_peras = int(input("Digiite a quantidade de peras: "))
custo_total = (quantidade_macas*0.30) + (quantidade_peras*0.25)
print(f'O custo total é de {custo_total}')

#Exercício 13: Solicite o nome de um produto e seu preço, e exiba uma mensagem informando o nome do produto e o preço com 10% de desconto.

produto = str(input("Digite o nome do produto: "))
preco = float(input("Digite o preço do produto: "))
preco_com_desconto = (preco*10)/100
print(f"O preço do {produto} com 10% de desconto equivale a {preco_com_desconto}")
























