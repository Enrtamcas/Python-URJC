from random import randint


def selectMin(candidates, visited):
    vertex = None
    weight = float('inf')
    for i in range(len(candidates)):
        if not visited[i] and candidates[i] < weight:
            vertex = i
            weight = candidates[i]
    return vertex, weight


def prim(g):
    n = len(g)
    initial = randint(0, len(g) - 1)
    visited = [False] * n
    sol = 0
    visited[initial] = True
    candidates = [float('inf')] * n
    for (start, end, weight) in g[initial]:
        candidates[end] = weight
    for i in range(1, n):
        nextNode, cost = selectMin(candidates, visited)
        if cost < float('inf'):
            sol += cost
            visited[nextNode] = True
        for start, end, weight in g[nextNode]:
            if not visited[end]:
                candidates[end] = min(weight, candidates[end])
    return sol


g = [
    [(0, 1, 2), (0, 3, 6)],  # edges from node 0
    [(1, 0, 2), (1, 2, 3)],  # edges from node 1
    [(2, 1, 3), (2, 3, 1)],  # edges from node 2
    [(3, 0, 6), (3, 2, 1)]   # edges from node 3
]


sol = prim(g)
print(sol)
