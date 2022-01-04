# Exercício 4.9 - Escreva um programa para aprovar o empréstimo bancário para comprar uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.
valorCasa = float(input("Digite o valor da casa: R$"))
salario = float(input("Digite o seu salário: R$"))
qtdAnosPagando = int(input("Digite a quantidade de anos a pagar: "))
qtdMesesPagando = qtdAnosPagando * 12
valorPrestacao = valorCasa / qtdMesesPagando
if valorPrestacao > 0.30 * salario:
    print("Empréstimo negado.")
else:
    print("Empréstimo aprovado.")