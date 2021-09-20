def converteKmtoMil(km: float) -> float:
    mil = km/1.61
    return mil


print("A velocidade em Milhas é de: {:.1f}" .format(
    converteKmtoMil(float(input("Digite a velocidade em Km/h: ")))))
