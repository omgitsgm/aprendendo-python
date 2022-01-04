# Exercício 4.10 - Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela do livro.
# Gabriel Mendes, 04.01.2022
qtd_kWh = float(input("Digite a quantidade de kWh consumida: "))
tipoInstalacao = input("Qual é o tipo de instalação?\nR - residências\nC - comércios\nI - indústrias\nDigite a letra inicial do tipo de instalação: ")
if tipoInstalacao == 'R':
    if qtd_kWh <= 500:
        preco = qtd_kWh * 0.40
    else:
        preco = qtd_kWh * 0.65
elif tipoInstalacao == 'C':
    if qtd_kWh <= 1000:
        preco = qtd_kWh * 0.55
    else:
        preco = qtd_kWh * 0.60
elif tipoInstalacao == 'I':
    if qtd_kWh <= 5000:
        preco = qtd_kWh * 0.55
    else:
        preco = qtd_kWh * 0.60
else:
    print("Tipo de instalação inválida. Digite 'R', 'C' ou 'I'.")
    preco = 0
print(f"O valor a ser pago é de R${preco:5.2f}.")