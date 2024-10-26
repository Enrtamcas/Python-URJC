def sortCandidates(g):
    candidates = []
    for adj in g:
        for (start, end, weight) in adj:
            candidates.append((weight, start, end))
    candidates.sort()
    return candidates


def update(g, start, end):
    for i in range(len(g)):
        if g[i] == end:
            g[i] = start


def function(g):
    candidates = sortCandidates(g)
    second_graph = list(range(len(g)))

    sol = 0
    count = len(second_graph) - 1
    i = 0

    while count > 0 and i < len(candidates):
        (start, end, weight) = candidates[i]
        if second_graph[start] != second_graph[end]:
            sol += weight
            count -= 1
            update(second_graph, candidates[start], candidates[end])
        i += 1
    return sol


if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    g = [[] for i in range(n)]

    for _ in range(m):
        n1, n2, d = map(int, input().strip().split())
        g[n1].append((n1, n2, d))

    sol = function(g)
    print(g)
