def conversaoCeltoFah(c: float) -> float:
    f = c * (9.0/5.0) + 32.0
    return f


print('A temperatura em Fahrenheit é: {:.1f}°F' .format(
    conversaoCeltoFah(float(input('Digite a temperatura em graus Celcius: ')))))
