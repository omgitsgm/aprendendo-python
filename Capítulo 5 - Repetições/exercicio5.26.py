# Exercício 5.26 - Escreva um programa que calcule o resto da divisão inteira entre dois números. Utilize apenas as operações de soma e subtração para calcular o resultado.
# Gabriel Mendes, 09.01.2022
primeiroNumero = float(input("Digite o primeiro número: "))
segundoNumero = float(input("Digite o segundo número: "))
dividendo = primeiroNumero
resultado = 0
while dividendo >= segundoNumero:
    dividendo -= segundoNumero
    resultado += 1
resto = primeiroNumero - (segundoNumero * resultado)
print(f"{primeiroNumero} // {segundoNumero} = {resultado} e resto {resto}")