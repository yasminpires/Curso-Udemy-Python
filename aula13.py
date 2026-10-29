nome = 'Yasmin Pires'
altura = 1.57
peso = 64
imc = peso / altura ** 2  # IMC = peso / (altura x altura)

linha_1 = f'{nome} tem {altura: .2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc: .2f}'

print (linha_1)
print (linha_2)
print (linha_3)


# Yasmin Pires tem 1.80 de altura,
# pesa 64 quilos e seu IMC é
# 25.96454217209623
