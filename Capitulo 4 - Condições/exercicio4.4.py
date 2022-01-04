# Exercício 4.4 - Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
salarioFuncionario = float(input("Digite o salário do funcionário: R$"))
if salarioFuncionario > 1_250.00:
    aumento = salarioFuncionario * (10 / 100)
if salarioFuncionario <= 1_250.00:
    aumento = salarioFuncionario * (15 / 100)
salarioFinal = salarioFuncionario + aumento
print(f"O salário inicial era de R${salarioFuncionario:5.2f}. Houve um aumento de R${aumento:5.2f}, por isso, o salário final é de R${salarioFinal:5.2f}.")