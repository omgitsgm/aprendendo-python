# Exercício 3.9 - Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
# Gabriel Mendes, 03.01.2022
qtdDias = int(input("Quantidade de dias: "))
qtdHoras = int(input("Quantidade de horas: "))
qtdMinutos = int(input("Quantidade de minutos: "))
qtdSegundos = int(input("Quantidade de segundos: "))

diasParaSegundos = ((qtdDias * 24) * 60) * 60 
horasParaSegundos = (qtdHoras * 60) * 60
minutosParaSegundos = qtdMinutos * 60
totalEmSegundos = diasParaSegundos + horasParaSegundos + minutosParaSegundos + qtdSegundos

print(f"O usuário possui {qtdDias} dia(s), {qtdHoras} hora(s), {qtdMinutos} minuto(s) e {qtdSegundos} segundo(s).")
print(f"Totaliza-se, então, {totalEmSegundos} segundo(s).")