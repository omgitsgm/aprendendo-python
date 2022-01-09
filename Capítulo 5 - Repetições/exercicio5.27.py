# Exercício 5.27 - Escreva um programa que verifique se um número é palíndromo. Um número é palíndromo se continua o mesmo caso seus número sejam invertidos. Exemplos: 454, 10501
# Gabriel Mendes, 09.01.2022
while True:
    numero = int(input("Digite um número inteiro (10 >= n <= 99.999): "))
    if numero < 10:
        print("Digite um número inteiro com, pelo menos, 2 algarismos.")
    elif numero > 99_999:
        print("Digite um número inteiro com, no máximo, 5 algarismos.")
    else: # Se o número for válido, sai do loop
        break
palindromo = False
if numero / 10_000 >= 1.0: # Verifica se o número possui 5 algarismos
    primeiroAlgarismo = numero // 10_000
    resto = numero % 10_000
    segundoAlgarismo = resto // 1_000
    resto = resto % 1_000
    terceiroAlgarismo = resto // 100
    resto = resto % 100
    quartoAlgarismo = resto // 10
    quintoAlgarismo = resto % 10
    if primeiroAlgarismo == quintoAlgarismo and segundoAlgarismo == quartoAlgarismo:
        palindromo = True
elif numero / 1_000 >= 1.0: # Verfiica se o número possui 4 algarismos
    primeiroAlgarismo = numero // 1_000
    resto = numero % 1_000
    segundoAlgarismo = resto // 100
    resto = numero % 100
    terceiroAlgarismo = resto // 10
    quartoAlgarismo = numero % 10
    if primeiroAlgarismo == quartoAlgarismo and segundoAlgarismo == terceiroAlgarismo:
        palindromo = True
elif numero / 100 >= 1.0: # Verfiica se o número possui 3 algarismos
    primeiroAlgarismo = numero // 100
    resto = numero % 100
    segundoAlgarismo = resto // 10
    terceiroAlgarismo = numero % 10
    if primeiroAlgarismo == terceiroAlgarismo:
        palindromo = True
elif numero / 10 >= 1.0: # Verfiica se o número possui 2 algarismos
    primeiroAlgarismo = numero // 10
    segundoAlgarismo = numero % 10
    if primeiroAlgarismo == segundoAlgarismo:
        palindromo = True
if palindromo == True:
    print(f"O número {numero} é um palíndromo.")
else:
    print(f"O número {numero} não é um palíndromo.")