def selectMinDistance(distances, visited):
    min_distance = float('inf')
    min_index = -1
    for i in range(len(distances)):
        if not visited[i] and distances[i] < min_distance:
            min_distance = distances[i]
            min_index = i
    return min_index


def dijkstra(g, origin):
    n = len(g)
    distances = [float('inf')] * n
    visited = [False] * n

    distances[origin] = 0
    visited[origin] = True

    for end, weight in g[origin]:
        distances[end] = min(distances[end], weight)
    for _ in range(n):
        nextNode = selectMinDistance(distances, visited)
        visited[nextNode] = True
        for end, weight in g[nextNode]:
            distances[end] = min(distances[end], distances[nextNode] + weight)

    return distances


if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    types = list(map(int, input().strip().split()))
    g = []
    for _ in range(n):
        g.append([])
    for _ in range(m):
        c, d, l = map(int, input().strip().split())
        g[c].append((d, l))
        g[d].append((c, l))

    min_distances = [float('inf')] * (max(types) + 1)
    print(min_distances)

    print(types)
    print("types de 0:", types.count(0))
    print("types de 1:", types.count(1))
    for i in range(n):
        if types.count(types[i]) > 1:
            distances = dijkstra(g, i)
            for j in range(n):
                if i != j and types[i] == types[j]:
                    min_distances[types[i]] = min(min_distances[types[i]], distances[j])

    distancias_minimas_simples = []
    for d in min_distances:
        if d != float('inf'):
            distancias_minimas_simples.append(str(d))
        else:
            distancias_minimas_simples.append('-1')
    result = ' '.join(distancias_minimas_simples)
    print(result)
