def advance_deleted_list(v, deleted, deleted_id):
    while deleted[deleted_id] and deleted_id < len(v) - 1:
        deleted_id += 1
    deleted[deleted_id] = True


def binary_search(v, ini, fin, x, deleted):
    if ini > fin:
        deleted_id = ini
        advance_deleted_list(v, deleted, deleted_id)
        return deleted_id

    mid = (ini + fin) // 2
    if x == v[mid]:
        deleted_id = mid
        advance_deleted_list(v, deleted, deleted_id)
        return deleted_id
    elif x > v[mid]:
        return binary_search(v, mid + 1, fin, x, deleted)
    else:
        return binary_search(v, ini, mid - 1, x, deleted)


if __name__ == "__main__":
    n = int(input().strip())

    rejilla = [[]] * n
    eliminados = [False] * (n * n)
    id_players = []

    for i in range(n):
        rejilla[i] = list(map(int, input().strip().split()))

    for i in range(n):
        for j in range(n):
            id_players.append(rejilla[i][j])

    selected_players = list(map(int, input().strip().split()))

    for target in selected_players:
        pos = binary_search(id_players, 0, len(id_players) - 1, target, eliminados)

    cont = 0
    for i in range(n):
        for j in range(n):
            if eliminados[cont]:
                print("X", end=' ')
            else:
                print(rejilla[i][j], end=' ')
            cont += 1
        print()
