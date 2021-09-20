# Constante de pi
pi = 3.14


def converteRadianotoGraus(rad: float) -> float:
    graus = rad * 180/pi
    return graus


print("Em Graus temos: {:.2f}º" .format(
    converteRadianotoGraus(float(input("Digite um ângulo em radianos: ")))))
