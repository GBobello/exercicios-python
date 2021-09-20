# Constante de pi
pi = 3.14


def converteGraustoRadiano(graus: float) -> float:
    rad = graus * pi/180
    return rad


print("Em radiano temos: {:.2f}" .format(
    converteGraustoRadiano(float(input("Digite um ângulo em graus: ")))))
