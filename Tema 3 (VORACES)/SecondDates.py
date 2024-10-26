def sol(data, n):
    equipo_jovenes = []
    for i in range(n):
        equipo_jovenes.append(data.pop(0))

    for _ in range(n):
        print(equipo_jovenes[_][1], end=' ')
    print()
    for c in data:
        print(c[1], end=' ')


if __name__ == "__main__":
    n, k = map(int, input().strip().split())

    data = []
    for _ in range(n):
        a, b = map(str, input().strip().split())
        b = int(b)
        data.append((b, a))
    data.sort()
    sol(data, min(n - k, k))

