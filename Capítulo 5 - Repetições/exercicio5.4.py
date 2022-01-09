# Exercício 5.4 - Faça um programa para imprimir de 1 até o número digitado pelo usuário, mas apenas os números ímpares.
# Gabriel Mendes, 04.01.2022
fim = int(input("Digite o valor final da contagem: "))
contagem = 1
while contagem <= fim:
    if contagem % 2 != 0:
        print(contagem)
    contagem = contagem + 1