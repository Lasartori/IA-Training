#Media de numeros
# numeros = [10,20,30,40,50]
# soma = 0

# soma = sum(numeros)
# media = soma / len(numeros)

# print(media)

# Quem gastou mais
# gastos_joao = [300, 500, 200, 800]
# gastos_pedro = [200, 300, 500, 700]

# soma_joao = sum(gastos_joao)
# soma_pedro = sum(gastos_pedro)

# if soma_joao > soma_pedro:
#     print('João gastou mais dinheiro em um mês do que Pedro!')
# elif soma_pedro > soma_joao:
#     print('Pedro gastou mais dinheiro que João!')
# else:
#     print('Os dois gastaram a mesma quantidade!')

# Maior e menor palavra
# palavras = ["python", "asimov", "código", "web", "programação"]
# palavra_menor = palavras[0]
# palavra_maior = palavras[0]

# for palavra in palavras:
#     if len(palavra) > len(palavra_maior):
#         palavra_maior = palavra
#     if len(palavra) < len(palavra_menor):
#         palavra_menor = palavra 

# print('A menor palavra da Array é: '+ palavra_menor + ' e a maior palavra é: '+ palavra_maior)

#Encontre o segundo maior valor
# numeros = [32, 10, 58, 30, 55, 12, 28, 51]

# numeros.sort()

# segundo_maior = numeros[-2]
# print (segundo_maior)

#Resultado de pesquisa
# votos = ["A", "B", "A", "C", "C", "A", "C", "C", "B", "A"]

# frequencia = {}

# for produto in votos:
#     if produto in frequencia:
#         frequencia[produto] += 1
#     else:
#         frequencia[produto] = 1

# print(frequencia)

# Detector de Palindromos

# palavra = input('Digite a palavra para testar se é palindromo: ')

# palavra_invertida = palavra[::-1]

# if palavra == palavra_invertida:
#     print('A palavra é um palíndromo!')
# else:
#     print('Não é um palindromo!')

#Formatar os números de venda

# aumento_vendas = 32.048701
# formatado = str(round(aumento_vendas,2))
# print('O aumento percentual de vendas foi de ' + formatado + '%')

# Detector de spam

# def detector_spam(email):
#     if email.endswith('@xyz.com'):
#         print ('O e-mail é um spam')
#     else:
#         print('O e-mail é legítimo')

# detector_spam('sualoja@neo.com')
# detector_spam('sualoja@xyz.com')

#Indices do alfabeto
# def indice_alfabeto(indice):
#     alfabeto = 'abcdefghijklmnopqrstuvwxyz'

#     if 1 <= indice <= 26:
#         return alfabeto[indice -1]
#     else:
#         return ''
    
# print (indice_alfabeto(1))
# print (indice_alfabeto(3))
# print (indice_alfabeto(5))
# print (indice_alfabeto(23))

#Pegar dois números e calcular se o produto deles é maior que mil e realizar interações diferentes caso for
# number1 = int(input('Digite o primeiro número: '))
# number2 = int(input('Digite o segundo número número: '))

# def numbers(number1,number2):
#     numeros = number1 * number2
#     if numeros <= 1000:
#         return numeros
#     else:
#         soma = number1 + number2
#         return soma
 
# result = numbers(number1, number2)
# print(f'The result is {result}')

#De 0 a 10 somando com o anterior

# previous = 0
# for i in range(10):
#     sum = i + previous
#     print(f'Current number {i} | Previous number {previous} | Sum: {sum}')
#     previous = i

#Remover n caracteres de uma string

# palavra = input('Digite a palavra: ')
# n = int(input('Digite a quantidade de caracteres a serem removidos: '))


# def remove_chars(s,n):
#     if n <= 0 :
#         print('Erro: O valor ñao pode ser menor ou igual a 0.')
#         return s
    
#     elif n >= len(s):
#         print('O valor de caracteres não pode ser igual ou maior a palavra!')
#         return s
#     else:
#         return s[n:]
    
# resultado = remove_chars(palavra,n)
# print(f'Nova String: {resultado}')


#Calculadora

operation = int(input ('Qual operação você quer realizar?\n 1 - Adição\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão\n Operação:'))
if operation < 0 or operation >= 5:
    print('Digite um valor válido!')
    exit()
try:
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
except ValueError:
    print('Você precisa digitar um valor válido!')
    exit()



if operation == 1:
    valor = num1 + num2
    print(f'o resultado é: {valor}')
elif operation == 2:
    valor = num1 - num2
    print(f'o resultado é: {valor}')
elif operation == 3:
    valor = num1 * num2
    print(f'o resultado é: {valor}')
elif operation == 4:
    if num1 == 0 or num2 == 0:
        print('Não pode ser dividido um número por zero!')
    else:
        valor = num1 / num2
        print(f'O resultado é: {valor}')


