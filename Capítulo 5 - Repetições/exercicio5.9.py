# Exercício 5.9 - Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender o quociente de uma divisão de dois números como a quantidade de vezes que podemos retirar o divisor do dividendo. Logo, 20 / 4 = 5, uma vez que podermos subtrair 4 cinco vezes de 20.
# Gabriel Mendes, 04.01.2022
primeiroValor = int(input("Digite o primeiro valor: ")) # 20 -> dividendo
segundoValor = int(input("Digite o segundo valor: ")) # 4 -> divisor
dividendo = primeiroValor
divisor = segundoValor
resultado = 0
if dividendo >= divisor:
    while dividendo >= divisor:
        dividendo = dividendo - divisor
        resto = dividendo
        resultado = resultado + 1
else:
    resto = dividendo

print(f"{primeiroValor} / {segundoValor} = {resultado}, com resto {resto}.")