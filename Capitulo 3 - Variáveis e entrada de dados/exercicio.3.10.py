# Exercício 3.10 - Faça um programa que calcula o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
# Gabriel Mendes, 03.01.2022
salario = float(input("Digite o salário: R$"))
porcentagemAumento = (float(input("Digite o percentual do aumento: "))) / 100
valorAumento = salario * porcentagemAumento
novoSalario = salario + valorAumento
print(f"O valor do aumento será de R${valorAumento:5.2f}. O novo salário é R${novoSalario:5.2f}.")