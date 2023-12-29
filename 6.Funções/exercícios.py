# '''
# Crie uma função que recebe dois números como parâmetros e retorna a sua soma.


# '''

# def soma(num1,num2):
#     return num1+num2
    
# num1 = int(input("Digite um número: "))
# num2 = int(input("Digite um segundo número"))

# print(soma(num1,num2))

# '''
# Escreva uma função que recebe um nome como parâmetro e imprime uma saudação personalizada.

# '''
# def saudacao_personalizada(nome):
#     return f"Seja bem vindo(a) {nome}"

# nome_do_usuario = input("Digite seu nome: ")
# print(saudacao_personalizada(nome_do_usuario))
# '''

# Implemente uma função que verifica se um número é par. A função deve retornar True se for par, e False caso contrário.


# '''

# def eh_par(numero):
#     if numero%2==0:
#         return True
#     else:
#         return False

# valor = int(input('Digite o número que gostaria de descobrir se é par ou ímpar: '))
# print(eh_par(valor))


# '''
# Crie uma função que calcula a média de três números passados como argumentos.

# '''

# def encontrar_media(numero1,numero2,numero3):
#     soma = numero1 +numero2 + numero3
#     media = soma/3
#     return media

# n1 = int(input("Digite um número: "))
# n2 = int(input("Digite um outro número: "))
# n3 = int(input("Digite mais um número: "))

# print(encontrar_media(n1,n2,n3))

# '''
# Escreva uma função que recebe um número e retorna o seu quadrado.

'''
# def quadrado(x):
#     return x**x

# numero = int(input("Digite o número que gostaria de ver o quadrado: "))
# print(quadrado(numero))

# '''
# Implemente uma função que aceita um raio e calcula a área de um círculo.

# '''
# def calculo_area(raio):
#     pi = 3.14
#     return (raio**raio)*pi

# valor_do_raio = int(input("Digite o valor do raio: "))
# print(calculo_area(valor_do_raio))

# '''

# Crie uma função que recebe uma lista de números e retorna o maior deles.


# '''
# lista = []
# def maior_valor_da_lista():
#     for i in range(3):
#         lista.append(i)
#     return max(lista)

# print(maior_valor_da_lista())

'''

Escreva uma função que verifica se uma string é palíndromo.

'''
# def palindromo(palavra):
#     if palavra == palavra[::-1]:
#         return f"{palavra} é um palíndromo!"
    
# word = input("Digite a palavra para testar se é palíndromo: ")
# print(palindromo(word))


'''
Crie uma função que recebe uma lista de números e retorna a soma de todos os elementos.

'''
# def soma_dos_elementos():
#     lista1 = [1,2,3,4,5,6,7,8,9,10]
#     return sum(lista1)

# print(soma_dos_elementos())
'''
Escreva uma função que converte graus Celsius para Fahrenheit.

'''
# def conversao():
#     celsius = int(input("Digite o valor da temperatura em celsius: "))
#     F = celsius * 1.8 + 32
#     return F

'''
Implemente uma função que recebe uma lista e um valor, e retorna o número de ocorrências desse valor na lista.

'''
# def ocorrencias(lista,valor):
#     quantidade = lista.count(valor)
#     return f" O valor {valor} aparece {quantidade} vezes na lista"

# print(ocorrencias([1,2,2,2,2,3,4,5,6],2))
            

'''
Crie uma função que imprime os números pares de 1 a 20 usando um loop for.

'''

def imprimir():
    for i in range(1,21):
        print(i)

'''
Escreva uma função que aceita um número e retorna "positivo", "negativo" ou "zero" conforme o caso.
'''

# def valor(numero):
#     if numero >0:
#         return "Positivo"
#     elif numero <0:
#         return "Negativo"
#     else:
#         return "Nulo"

'''
Implemente uma função que recebe uma lista de palavras e retorna a quantidade de palavras que começam com a letra 'A'.

'''
# def palavras_com_letra_a(lista):
#     lista2 = []
#     for i in lista:
#         if i[0]=="a"or i[0] =="A":
#             lista2.append(i)
#     return lista2

# print(palavras_com_letra_a(["Ana","amor","Julia"]))
    

'''
Crie uma função que recebe uma lista de números e retorna uma nova lista com apenas os números pares.

'''
# def apenas_pares(lista):
#     lista3 = []
#     for i in lista:
#         if i%2==0:
#             lista3.append(i)
#     return lista3
            
'''

Escreva uma função que calcula o fatorial de um número.

'''

# def fatorial():
#     f = 1
#     numero = int(input("Digite o número que gostaria de ver o fatorial: "))
#     for i in range(numero,1,-1):
#         print(f" 5 X {i} = {5*i}")
#         f*=i
#     return f

# print(fatorial())
        
'''
Implemente uma função que recebe uma string e retorna a mesma string invertida.

'''

# def string_invertida():
#     string = input("Digite a palavra que gostaria de inverter: ")
#     return string[::-1]

# print(string_invertida())


'''
Crie uma função que imprime os números ímpares de 1 a 30 usando um loop while.
'''
# def impares():
#     contador = 0
#     while contador <31:
#         print(contador)
#         contador+=1
        
# impares()
    
'''
Escreva uma função que aceita um número e retorna "primo" ou "não primo".
'''
def eh_primo(numero):
    if numero < 2:
        return "não primo"
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return "não primo"
    return "primo"


'''
Implemente uma função que recebe uma lista de números e retorna a média.
'''

# def media(lista):
#     soma = sum(lista)
#     print(soma)
#     tamanho_da_lista = len(lista)
#     print(tamanho_da_lista)
#     media = soma/tamanho_da_lista
#     return f'{media:.1f}'

# print(media([1,2,3,4,5,6,10]))
'''
Crie uma função que recebe dois números e retorna o menor deles.
'''
# def menor_deles(num1,num2):
#     if num1 <num2:
#         return num1
#     else:
#         return num2
    

'''
Escreva uma função que verifica se uma palavra é um anagrama de outra.
'''
# def anagrama(palavra1,palavra2):
#     for i in palavra1:
        

'''
Implemente uma função que recebe um número e retorna a sequência de Fibonacci até esse número.

'''
def fibonacci_ate_n(numero):
    a, b = 0, 1
    while a <= numero:
        print(a, end=' ')
        a, b = b, a + b
    
    


'''

Crie uma função que imprime os números de 10 a 1 usando um loop for.

'''
def loop():
    for i in range(10,0,1):
        print(i)

'''

Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados.

'''
def sem_duplicatas(lista):
    for i in lista:
        repeticao = lista.count(i)
        if repeticao>0:
            lista.remove(i)
        
    return lista
    
'''
Implemente uma função que converte uma string para maiúsculas.

'''
# def maiusculas():
#     string = input('Digite a palavra que quer deixar maiúscula: ').upper()
#     print(string)


'''

Crie uma função que recebe uma lista de números e retorna o produto de todos os elementos.
'''
def produto_elementos(lista):
    if not lista:
        return None  # Retorna None se a lista estiver vazia
    resultado = 1
    for numero in lista:
        resultado *= numero
    return resultado

'''
Escreva uma função que recebe uma lista de strings e retorna a string mais longa.

'''
# def mais_longa(lista):
#     maior_palavra = ""
#     for palavra in lista:
#         if  len(palavra) > len(maior_palavra):
#             maior_palavra = palavra
#     return maior_palavra
    
# print(mais_longa(["Nathalia","gisa","pindamonhagaba"]))
'''
Implemente uma função que aceita um número e retorna "par" se for par, "ímpar" se for ímpar.


'''
# def num(numero):
#     if numero%2==0:
#         return "Par"
#     else:
#         return "Ímpar"
    
'''
Crie uma função que imprime os números múltiplos de 3 de 1 a 50 usando um loop while.
'''
def multiplos_de_tres():
    numero = 1
    while numero <= 50:
        if numero % 3 == 0:
            print(numero)
        numero += 1




'''
Escreva uma função que inverte a ordem dos elementos em uma lista.
'''

# def lista_invertida(lista):
#     lista.reverse()
#     return lista

'''
Implemente uma função que recebe um número e retorna a soma dos seus dígitos.

'''
# lista_strings = []
# lista_numeros = []
# def soma_dos_numeros(numero):
#     string = str(numero)
#     for i in string:
#         numero = int(i)
#         lista_numeros.append(numero)
#     return sum(lista_numeros)

# print(soma_dos_numeros(123))

'''
Crie uma função que recebe duas listas e retorna uma nova lista com os elementos comuns a ambas.

'''
# lista3 = []
# def ambos(lista1,lista2):
#     for i in lista1:
#         if i in lista2:
#           lista3.append(i)
          
#     return lista3  

# print(ambos([1,4,5,6],[1,2,3,4,7]))

'''

Escreva uma função que recebe uma string e retorna a quantidade de vogais.

'''

# def quantidade_de_vogais(string):
#     contador = 0
#     for i in string:
#         if i =="a" or i=="e" or i=="i" or i=="o" or i=="u":
#             contador+=1
#     return f' tem {contador} vogais'

# print(quantidade_de_vogais("Nathalia"))
    

'''
Implemente uma função que calcula a potência de um número.

'''
# def potencia(x):
#     return x**x


'''

Crie uma função que imprime os números de 1 a 100, substituindo os múltiplos de 3 por "Fizz" e os múltiplos de 5 por "Buzz".

'''
def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)




'''
Escreva uma função que recebe uma lista de números e retorna a lista ordenada de forma crescente.

'''
# def organizar_lista(lista):
#     lista.sort()
#     return lista

'''
Implemente uma função que recebe um número e retorna a soma dos números naturais até esse número.
'''
def soma_naturais(numero):
    soma = 0
    for i in range(1, numero + 1):
        soma += i
    return soma
'''
Crie uma função que verifica se uma lista está ordenada de forma crescente.
'''
def verificar_lista(lista):
    lista_organizada = lista.sort()
    if lista == lista_organizada:
        return "Está organizada"
    else:
        return "Está desorganizada"
    
    

'''
Escreva uma função que recebe uma lista de números e retorna o segundo maior número.
'''

def segundo_maior(lista):
    lista.sort()
    
    return lista[2]



'''
Implemente uma função que recebe uma string e conta quantas vezes cada caractere aparece.

'''

lista = []
def repeticao_caracteres(string):
    for i in string:
        lista.append(i)
        
    for i in lista:
        quantidade = lista.count(i)
        print(f"A quantidade de letras {i} é de {quantidade}")
    
repeticao_caracteres("Nathalia")

'''
Crie uma função que imprime os números pares de 50 a 1 usando um loop while.

'''
numero = 50

while numero>-1:
    print(numero)
    numero-=1
'''

Escreva uma função que aceita uma lista de palavras e retorna uma nova lista com as palavras em ordem alfabética.

'''

def organizado(lista):
    lista.sort
    return lista
'''

Implemente uma função que recebe um número e retorna a soma dos seus divisores.
'''

def soma_divisores(numero):
    soma = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            soma += i
    return soma

'''
Escreva uma função que inverte as palavras em uma frase.
'''
def inverter(frase):
    return frase[::-1]


'''
Implemente uma função que recebe uma lista de números e retorna a lista invertida.
'''
def inverter_lista(lista):
    lista.reverse()
    return lista

'''
Crie uma função que recebe uma lista de strings e retorna uma nova lista com as strings concatenadas.

'''

def concatenadas(lista):
    palavras_juntas=""
    for i in lista:
        palavras_juntas+=i
        


'''
Escreva uma função que verifica se uma lista contém apenas números primos.



'''

def eprimo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def apenas_primos(lst):
    for num in lst:
        if not eprimo(num):
            return False
    return True
    
    
    
