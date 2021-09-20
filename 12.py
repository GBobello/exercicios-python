def converteMiltoKm(mil: float) -> float:
    km = 1.61 * mil
    return km


print("A velocidade em Km/h é: {:.1f} Km/h" .format(
    converteMiltoKm(float(input('Digite a velocidade em milhas: ')))))
