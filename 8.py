def converteKeltoCel(k: float) -> float:
    c = k - 273.15
    return c


print('A temperatura em Celcius é: {:.1f}ºC' .format(
    converteKeltoCel(float(input('Digite uma temperatura em Kelvin: ')))))
