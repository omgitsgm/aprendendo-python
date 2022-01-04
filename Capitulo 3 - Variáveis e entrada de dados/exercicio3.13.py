# Exercício 3.13 - Escreva um programa que converta uma temperatura digitada em graus Celsius em graus Farenheit. A fórmula para essa conversão é: F = (9 * C / 5) + 32
temperaturaCelsius = float(input("Digite uma temperatura em graus Celsius: "))
temperaturaFahrenheit = (9 * temperaturaCelsius / 5) + 32
print(f"{temperaturaCelsius} graus Celsius, em Fahrenheit é igual a {temperaturaFahrenheit}F.")