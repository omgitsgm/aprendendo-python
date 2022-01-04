# Exercício 4.2 - Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$5 por km acima de 80km/h.
# Gabriel Mendes, 03.01.2022
velocidadeCarro = float(input("Digite a velocidade do carro (km/h): "))
if velocidadeCarro > 80:
    print("Você foi multado :(")
    valorMulta = (velocidadeCarro - 80) * 5
    print(f"O valor da multa é de R${valorMulta:5.2f}.")
if velocidadeCarro <= 80:
    print("Você não foi multado :)")