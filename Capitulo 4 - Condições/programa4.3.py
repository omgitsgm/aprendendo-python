# Programa 4.3 - Cálculo do Imposto de Renda
# Gabriel Mendes, 03.01.2022
salario = float(input("Digite o salário para cálculo do imposto: "))
base = salario
imposto = 0
if base > 3_000:
    imposto = imposto + ((base - 3000) * 0.35) # imposto = 0 + ((4000 - 3000) * 0.35) -> 1000 * 0.35 = 350
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20) # imposto = 350 + ((3000 - 1000) * 0.20) -> 350 + 2000 * 0.20 = 750
print(f"Salário: R${salario:6.2f} || Imposto a pagar: R${imposto:6.2f}")