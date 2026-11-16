import math
# x = Gewinnrate des Knotens
# n = Anzahl der Simulationen, die von diesem Knoten ausgehen
# C = Konstante
# N = Anzahl der Simulationen des Elternknotens

def uct(x, n, N):
    C = 2
    result = x + C * math.sqrt(math.log(N) / n)

    return result

print(uct(2, 1, 4))