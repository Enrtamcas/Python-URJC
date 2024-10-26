from collections import deque


def construirmatrizady(tablero):
    filas = len(tablero)
    columnas = len(tablero[0])
    enemigos = [(f, c) for f in range(filas) for c in range(columnas) if tablero[f][c] == 1 or tablero[f][c] == 2]
    num_enemigos = len(enemigos)

    matrizdist = [[float("inf")] * num_enemigos for _ in range(num_enemigos)]

    for r in range(num_enemigos):
        cola = deque([(enemigos[r], 0)])
        visitados = set()
        while cola:
            (fila, col), distancia_actual = cola.popleft()
            if (fila, col) in visitados:
                continue
            visitados.add((fila, col))

            if tablero[fila][col] == 1 or tablero[fila][col] == 2:
                indice_enemigo = enemigos.index((fila, col))
                matrizdist[r][indice_enemigo] = distancia_actual

            for despl_fila, despl_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nueva_fila, nueva_col = fila + despl_fila, col + despl_col
                if 0 <= nueva_fila < filas and 0 <= nueva_col < columnas and tablero[nueva_fila][nueva_col] != -1 and (
                nueva_fila, nueva_col) not in visitados:
                    cola.append(((nueva_fila, nueva_col), distancia_actual + 1))

    return matrizdist


def caballeroscuro(matriz, nodo_actual, visitados, camino_actual, dist_actual, dist_minima, camino_minimo):
    if all(visitados):
        if dist_actual < dist_minima[0]:
            camino_minimo[:] = camino_actual
            dist_minima[0] = dist_actual
        return

    for siguiente in range(len(matriz)):
        if not visitados[siguiente]:
            visitados[siguiente] = True
            camino_actual.append(siguiente)
            caballeroscuro(matriz, siguiente, visitados, camino_actual, dist_actual + matriz[nodo_actual][siguiente],
                           dist_minima, camino_minimo)
            visitados[siguiente] = False
            camino_actual.pop()


if __name__ == "__main__":
    tablero = []
    n, m, e = map(int, input().strip().split())
    for i in range(n):
        numbers = list(map(int, input().strip().split()))
        tablero.append(numbers)
    x, y, d = map(int, input().strip().split())
    tablero[x][y] = 2

    matrizdist = construirmatrizady(tablero)

    p = 0
    cab = False
    for i in range(n):
        for j in range(m):
            if tablero[i][j] == 1 and not cab:
                p += 1
            elif tablero[i][j] == 2:
                cab = True

    n = len(matrizdist)
    visitados = [False] * n
    visitados[p] = True
    camino_actual = [p]
    dist_minima = [float("inf")]
    camino_minimo = []

    caballeroscuro(matrizdist, p, visitados, camino_actual, 0, dist_minima, camino_minimo)

    if dist_minima[0] > d:
        print("CORRE")
    else:
        print("ATACA")
