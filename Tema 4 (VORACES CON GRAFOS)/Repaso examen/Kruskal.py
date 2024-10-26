def sortCandidates(g):
    candidates = []
    for adj in g:
        for start, end, weight in adj:
            candidates.append((weight, start, end))
    candidates.sort()
    return candidates


def update(sub_graph, start, end):
    for i in range(len(sub_graph)):
        if sub_graph[i] == end:
            sub_graph[i] = start


def kruskal(g):
    n = len(g)
    candidates = sortCandidates(g)
    sub_graph = list(range(n))
    count = n - 1
    sol = 0
    i = 0

    while count > 0 and i < n:
        weight, start, end = candidates[i]
        if sub_graph[start] != sub_graph[end]:
            count -= 1
            sol += weight
            update(sub_graph, sub_graph[start], sub_graph[end])
        i += 1
    return sol