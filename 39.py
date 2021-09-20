valor = 780000.00

valor1 = (valor * 46) / 100
valor2 = (valor * 32) / 100
valor3 = valor - valor1
valor3 = valor3 - valor2

print('O vencedor 1 receberá: R$ {:.2f}' .format(valor1))
print('O vencedor 2 receberá: R$ {:.2f}' .format(valor2))
print('O vencedor 3 receberá: R$ {:.2f}' .format(valor3))
