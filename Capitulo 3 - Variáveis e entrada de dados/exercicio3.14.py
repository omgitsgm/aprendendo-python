# Exercício 3.14 - Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.
# Gabriel Mendes, 03.01.2022
kmPercorridos = float(input("Digite a quantidade de km percorridos: "))
diasAlugado = int(input("Digite a quantidade de dias pelos quais o carro foi alugado: "))
diariaCarro = diasAlugado * 60
precoKm = kmPercorridos * 0.15
precoFinal = diariaCarro + precoKm
print(f"O carro percorreu {kmPercorridos:4.2f}km e foi alugado por {diasAlugado:02d} dias. O preço final é de R${precoFinal:5.2f}")