import math


def sortCandidates(g):
    candidates = []
    for adjs in g:
        for (start, end, weight) in adjs:
            candidates.append((weight, start, end))
    candidates.sort()
    return candidates


def updateComponents(components, new_id, old_id):
    for i in range(len(components)):
        if components[i] == old_id:
            components[i] = new_id


def function(g):
    candidates = sortCandidates(g)
    components = list(range(len(g)))  # crea un array [0,1,2, ..., 7]
    count = len(components) - 1  # resto 1, porque el array empieza en 0
    sol = 0
    # bucle voraz
    i = 0

    while count > 0 and len(candidates) > i:  # isSol
        (weight, start, end) = candidates[i]  # getBestItem
        if components[start] != components[end]:
            sol += weight
            count -= 1
            updateComponents(components, components[start], components[end])
        i += 1
    return sol


if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        n1, n2, d = map(int, input().strip().split())
        g[n1].append((n1, n2, d))

    sol = function(g)
    sol = math.ceil(sol / 5)
    print(sol)
