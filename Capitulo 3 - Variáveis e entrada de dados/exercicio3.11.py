# Exercício 3.11 - Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
# Gabriel Mendes, 03.01.2022
precoMercadoria = float(input("Digite o preço da mercadoria: R$"))
percentualDesconto = (float(input("Digite o percentual de desconto: "))) / 100
valorDesconto = precoMercadoria * percentualDesconto
precoFinal = precoMercadoria - valorDesconto
print(f"O valor do desconto é R${valorDesconto:5.2f}. O preço a pagar é R${precoFinal:5.2f}.")