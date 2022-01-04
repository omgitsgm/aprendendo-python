# Exercício 4.6 - Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até de 200km, e R$0,45 para viagens mais longas.
# Gabriel Mendes, 04.01.2022
distanciaPercorrida = float(input("Digite a distância que deseja percorrer em km: "))
if distanciaPercorrida <= 200:
    precoPassagem = distanciaPercorrida * 0.50
else:
    precoPassagem = distanciaPercorrida * 0.45
print(f"O preço da passagem é R${precoPassagem:4.2f}")