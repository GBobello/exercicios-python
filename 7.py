def converteFahtoCel(f: float) -> float:
    c = 5.0 * (f - 32.0)/9.0
    return c


print('A temperatura em Celcius é: {:.1f}ºC' .format(
    converteFahtoCel(float(input("Digite a temperatura em Fahrenheit: ")))))
