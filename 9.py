def converteCeltoKel(c: float) -> float:
    k = c + 273.15
    return k


print('A temperatura em Kelvin é: {:.2f}K' .format(
    converteCeltoKel(float(input("Digite uma temperatura em Celcius: ")))))
