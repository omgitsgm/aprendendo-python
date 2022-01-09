# Exercício 5.8 - Escreva um programa que leia dois números. Imprima o resultado a multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação e dois números como somas sucessivas de um deles. Assim, 4 x 3 = 4 + 4 + 4 = 3 + 3 + 3 + 3
# Gabriel Mendes, 04.01.2022
primeiroValor = int(input("Digite o primeiro valor: "))
segundoValor = int(input("Digite o segundo valor: "))
count = 0
resultado = 0
while count < segundoValor:
    resultado = resultado + primeiroValor
    count = count + 1
print(f"{primeiroValor} x {segundoValor} = {resultado}")