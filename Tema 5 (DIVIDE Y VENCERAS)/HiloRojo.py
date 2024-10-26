def binary_search(v, ini, fin, x):
    if ini > fin:
        return -1

    mid = (ini + fin) // 2

    if x == v[mid]:
        return mid
    elif x > v[mid]:
        return binary_search(v, mid + 1, fin, x)
    else:
        return binary_search(v, ini, mid - 1, x)


if __name__ == '__main__':
    n1 = int(input().strip())
    g1 = list(map(int, input().strip().split()))
    n2 = int(input().strip())
    g2 = list(map(int, input().strip().split()))


    p = int(input().strip())

    for _ in range(p):
        a, b = map(int, input().strip().split())
        mid_a = binary_search(g1, 0, len(g1) - 1, a)
        mid_b = binary_search(g2, 0, len(g2) - 1, b)

        if mid_b == -1 or mid_a == -1:
            print("SIN DESTINO")
        else:
            print(mid_a, mid_b)
