# Exercício 5.14 - Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.
# Gabriel Mendes, 05.01.2022
qtdNumeros = 0
soma = 0
while True:
    numero = int(input("Digite um número a somar ou digite '0' para sair: "))
    if numero == 0:
        break
    soma += numero
    qtdNumeros += 1
mediaAritmetica = soma / qtdNumeros
print(f"Quantidade de números digitados: {qtdNumeros}\nSoma dos números: {soma}\nMédia aritmética: {mediaAritmetica:2.1f}")