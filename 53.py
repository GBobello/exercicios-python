c = float(input("Digite o comprimento do terreno: "))
l = float(input("Digite a largura do terreno: "))
p = float(input("Digite o preço do metro de tela: "))

pComp = c * p
pLarg = l * p

pTotal = pComp + pLarg

print("O valor para cercar esse terreno deve ser dê: R${:.2f}" .format(pTotal))

'''
Acredito que o terreno deva ter mais do que dois lados, 
então o resultado com 4 lados seria:
'''

pComp = (c * 2) * p
pLarg = (l * 2) * p

pTotal = pComp + pLarg

print(
    "O valor para cercar este terreno caso tenha 4 lados, deve ser dê: R${:.2f}" .format(pTotal))
