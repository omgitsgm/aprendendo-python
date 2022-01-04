# Exercício 3.8 - Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.
# Gabriel Mendes, 03.01.2022
valorMetro = float(input("Digite um valor em metros: "))
metroParaMilimetro = valorMetro * 1_000
print(f"{valorMetro}m é igual a {metroParaMilimetro}mm.")