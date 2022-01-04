# Exercício 3.15 - Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
qtdCigarrosDia = int(input("Digite a quantidade de cigarros fumados por dia: "))
anosFumando = int(input("Digite a quantidade de anos que você já fuma: "))
minutosPerdidos = (qtdCigarrosDia * 10) * (anosFumando * 365)
diasPerdidos = (minutosPerdidos / 60) / 24
print(f"Ao fumar, você já perdeu, aproximadamente, {diasPerdidos:5.2f} dias de vida.")