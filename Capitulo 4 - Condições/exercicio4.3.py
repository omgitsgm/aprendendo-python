# Exercício 4.3 - Escreva um programa que leia três números e que imprima o maior e o menor.
# Gabriel Mendes, 03.01.2022
primeiroValor = int(input("Digite o primeiro valor: "))
segundoValor = int(input("Digite o segundo valor: "))
terceiroValor = int(input("Digite o terceiro valor: "))
if primeiroValor > segundoValor and primeiroValor > terceiroValor:
    maior = primeiroValor
    if segundoValor > terceiroValor:
        menor = terceiroValor
    if terceiroValor > segundoValor:
        menor = segundoValor
if segundoValor > primeiroValor and segundoValor > terceiroValor:
    maior = segundoValor
    if primeiroValor > terceiroValor:
        menor = terceiroValor
    if terceiroValor > primeiroValor:
        menor = primeiroValor
if terceiroValor > primeiroValor and terceiroValor > segundoValor:
    maior = terceiroValor
    if primeiroValor > segundoValor:
        menor = segundoValor
    if segundoValor > primeiroValor:
        menor = primeiroValor
print(f"O maior valor é {maior} e o menor valor é {menor}.")