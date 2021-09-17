def converteMstoKm(ms: float) -> float:
    km = ms * 3.6
    return km


print("A velocidade em Km/h é: {:.1f} Km/h" .format(
    converteMstoKm(float(input('Digite a velocidade em m/s: ')))))
