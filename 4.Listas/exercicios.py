'''
Exercícios de Fixação
'''

'''
Escreva um programa que recebe uma lista de números e retorna uma nova lista apenas com os números pares.
'''
# lista = []
# apenas_pares = []
# for i in range(5):
#     numero = int(input("Digite um número para ser adicionado na lista: "))
#     lista.append(numero)
# for numero in lista:
#     if numero%2==0:
#         apenas_pares.append(numero)

# print(apenas_pares)
    
'''
Escreva uma função que recebe uma lista de palavras e retorna uma nova lista contendo apenas as palavras que possuem mais de 5 caracteres.

'''
# lista_com_maiores = []
# def mais_que_cinco(lista):
#     for i in lista:
#         if len(i) > 5:
#             lista_com_maiores.append(i)
#     return lista_com_maiores

# print(mais_que_cinco(["Nathalia","Ana","Gisa"]))

'''
Escreva uma função que recebe duas listas e retorna uma nova lista contendo apenas os elementos comuns entre as duas listas.

'''
# lista3 = []
# def duas_listas(lista1,lista2):
#     for i in lista1:
#         if i in lista2:
#             lista3.append(i)
#     return lista3

# print(duas_listas([1,2,3,4,5],[2,4,6]))
'''
Escreva um programa que recebe uma lista de números e retorna a soma dos elementos em posições ímpares.

'''
# soma = 0
# lista = [1,2,3,4,5,6,7,8,9,10]
# for i in range(1,len(lista)+1,2):
#     soma+=lista[i]
# print(soma)

'''
Escreva um programa que recebe uma lista de strings e retorna uma nova lista contendo as strings invertidas.

'''

# lista_string = ["Aulas", "Back-End","Front-End","Programação"]
# lista_string_invertida = []

# for i in lista_string:
#     invertida = i[::-1]
#     lista_string_invertida.append(invertida)
# print(lista_string_invertida)

'''
Escreva uma função que recebe uma lista de números e retorna o segundo maior número da lista.

'''

# def segundo_maior(lista):
#     lista.sort()
#     return lista[1]

# print(segundo_maior([2,5,10]))

'''
Escreva um programa que recebe uma lista de nomes e retorna uma nova lista contendo apenas os nomes que começam com a letra "A".

'''

# lista_nomes = ["Agatha","Mirela","Nathalia","Marcus","Jake","Anabelle"]
# nomes_com_a = []
# for i in lista_nomes:
#     if i[0] == "a" or i[0]=="A":
#         nomes_com_a.append(i)
# print(nomes_com_a)

'''
Escreva uma função que recebe uma lista de números e retorna uma nova lista contendo apenas os números positivos.

'''

# lista = [1,2,3,4,-4,1/4,-2,-9]
# maiores_que_zero = []

# for i in lista:
#     if i > 0:
#         maiores_que_zero.append(i)
        
# print(maiores_que_zero)

'''
Escreva um programa que recebe duas listas e retorna uma nova lista contendo os elementos que aparecem em apenas uma das listas.

'''

# lista1 = [1,2,3,4,5,6]
# lista2 = [2,5,6,37,8,3]
# lista3 = []

# for i in lista1:
#     if i not in lista2:
#         lista3.append(i)
# print(lista3)

'''
Escreva um programa que recebe uma lista de números e retorna o número que aparece com mais frequência.

'''

# lista = [1,2,3,4,5,6,7,7,7,7,8,9,10,10,10]
# maior = 0
# for i in lista:
#     ocorrencias = lista.count(i)
#     if ocorrencias > maior:
#         maior = i
# print(maior)

'''
Escreva um programa que recebe uma lista de strings e retorna uma nova lista contendo apenas as strings que são palíndromos.

'''

# lista = ["anna", "hannah","ovo","Amiga"]
# palindromos = []

# for i in lista:
#     if i == i[::-1]:
#         palindromos.append(i)
# print(palindromos)

'''
Escreva um programa que recebe uma lista de nomes e retorna uma nova lista contendo apenas os nomes que terminam com a letra "s".

'''

# lista = ["Veritas","Luas","Magra"]
# finalS= []

# for i in lista:
#     posicao = len(i)
#     if i[posicao-1] =="s" or i[posicao-1]=="S":
#         finalS.append(i)
# print(finalS)