def converteKmtoMs(km: float) -> float:
    ms = km/3.6
    return ms


print("A velocidade em m/s é: {:.1f} m/s" .format(
    converteKmtoMs(float(input('Digite a velocidade em Km/h: ')))))
