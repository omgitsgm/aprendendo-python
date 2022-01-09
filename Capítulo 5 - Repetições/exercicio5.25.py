# Exercício 5.25 - Escreva um programa que calcule a raiz quadrada de um número. Utilize o método de Newton para obter um resultado aproximado. Sendo n o número a obter a raiz quadrada, considere a base b = 2. Calcule p usando a fórmula p = (b+(n/b))/2. Agora, calcule o quadrado de p. A cada passo, faça b = p e recalcule p usando a fórmula apresentada. Pare quando a diferença absoluta entre n e o quadrado de p for menor que 0,0001.
# Gabriel Mendes, 06.01.2022
n = float(input("Digite um número a obter a raiz quadrada: "))
b = 2
while abs(n - (p ** 2)) > 0.0001:
# Função abs calcula o valor absoluto de um número, ou seja, seu valor sem sinal.
    p = (b + (n / b)) / 2
    b = p
print(f"A raíz quadrada de {n} é igual a {p:8.4f}.")