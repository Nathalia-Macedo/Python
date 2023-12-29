#Exercícios Propostos
'''
Escreva um programa que crie uma tupla com 5 números inteiros e exiba os elementos da tupla na tela.

'''

# tupla = (1,2,3,4,5)

# for i in tupla:
#     print(i)

'''
Crie uma código que receba uma tupla e retorne a soma de todos os elementos.

'''

# tupla = (1,2,3,4,5)

# soma = 0
# for i in tupla:
#     soma+=i
# print(soma)

'''
Escreva um programa que crie duas tuplas e concatene-as em uma terceira tupla.

'''

# tupla1 = (1,2,3,4)
# tupla2 = (5,6,7,8)

# tupla3 = tupla1+tupla2

# print(tupla3)


'''
Crie um código que receba uma tupla de strings  e retorne a quantidade de palavras que começam com a letra "A".

'''

# tupla = ("Nathalia","Ana")
# contador = 0
# for i in tupla:
#     if i[0]=="A" or i[0]=="a":
#         contador +=1
# print(contador)

'''
Escreva um programa que crie uma tupla com 10 números e informe qual é o maior e o menor valor presente na tupla.


'''


# Criando uma tupla com 10 números (pode substituir pelos números desejados)
tupla_numeros = (5, 12, 8, 3, 20, 7, 15, 10, 1, 18)

# Inicializando as variáveis com o primeiro elemento da tupla
maior_valor = menor_valor = tupla_numeros[0]

# Iterando sobre os elementos da tupla, começando do segundo elemento
for numero in tupla_numeros[1:]:
    if numero > maior_valor:
        maior_valor = numero
    elif numero < menor_valor:
        menor_valor = numero

'''
Crie um código que receba uma tupla de números  e retorne outra tupla com os elementos em ordem inversa.
'''

def inverter_tupla(tupla):
    # Inicializa uma lista vazia para armazenar os elementos invertidos
    elementos_invertidos = []

    # Itera pela tupla de trás para frente e adiciona cada elemento à lista
    for i in range(len(tupla) - 1, -1, -1):
        elementos_invertidos.append(tupla[i])

    # Converte a lista de volta para uma tupla
    tupla_invertida = tuple(elementos_invertidos)
    
    return tupla_invertida

