def binary_search(v, ini, fin, x):
    if ini > fin:
        return (ini - 1)
    mid = (ini + fin) // 2
    if v[mid] == x:
        return mid
    if v[mid] < x:
        return binary_search(v, mid + 1, fin, x)
    else:
        return binary_search(v, ini, mid - 1, x)


if __name__ == '__main__':
    # Leer el primer número
    n = int(input().strip())

    # Leer la lista de números
    arr = list(map(int, input().strip().split()))

    accumulated_points = [0] * n
    aux = 0
    for i in range(len(arr)):
        aux += arr[i]
        accumulated_points[i] = aux
        
    n_test = int(input().strip())
    for _ in range(n_test):
        num = int(input().strip())
        myLastEnemy = binary_search(arr, 0, len(arr) - 1, num)

        if myLastEnemy == -1:
            print("0 0")
        elif myLastEnemy == len(arr):
            print(len(arr), accumulated_points[
                myLastEnemy - 1])
        else:
            print(myLastEnemy + 1, accumulated_points[myLastEnemy])
