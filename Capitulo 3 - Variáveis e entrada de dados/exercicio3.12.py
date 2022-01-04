# Exercício 3.12 - Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
# Gabriel Mendes, 03.01.2022
distanciaPercorrida = float(input("Digite a distância a percorrer (km): "))
velocidadeMedia = float(input("Difite a velocidade média esperada para a viagem (km/h): "))
duracaoViagem = distanciaPercorrida / velocidadeMedia
print(f"A duração da viagem será de, aproximadamente, {duracaoViagem}h.")