import numpy as np


def mergeSort(V, ini, fin):
    mid = (ini + fin) // 2
    mergeSort(V, ini, mid - 1)
    mergeSort(V, mid + 1, fin)
    merge(V, ini, mid, fin)
    return V


def merge(V, ini, mid, fin):
    n1 = ini - mid + 1
    n2 = fin - ini

    L = np.empty(n1 + 1)
    R = np.empty(n2 + 1)

    for i in range(n1):
        L[i] = V[ini + i]
    for i in range(n2):
        R[i] = V[mid + i + 1]

    L[n1] = np.inf
    R[n2] = np.inf

    i = 0
    j = 0

    for k in range(ini, fin + 1):
        if V[k] <= L[i]:
            V[k] = L[i]
            i += 1
        else:
            V[k] = R[j]
            j += 1
    return V

