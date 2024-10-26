def selectMinDistance(distances, visited):
    min_distance = float('inf')
    min_index = -1
    for i in range(len(distances)):
        if not visited[i] and distances[i] < min_distance:
            print("\t\tActualizando distancia")
            print("\t\tvisited:",visited)
            min_distance = distances[i]
            min_index = i
            print("\t\tdistances:",distances)
    print("\t\t++++++ RETURN:",min_index)
    return min_index

def dijkstra(g, origin):
    n = len(g)
    distances = [float('inf')] * n
    visited = [False] * n

    distances[origin] = 0
    visited[origin] = True

    for end, weight in g[origin]:
        distances[end] = min(distances[end], weight)

    print("g:",g)
    print("distances:",distances)
    for _ in range(n):
        print("\tIteracion dentro del bucle.")
        currentNode = selectMinDistance(distances, visited)
        visited[currentNode] = True
        for end, weight in g[currentNode]:
            print("\t\t\t distances:",distances)
            print("\t\t\t-------")
            print("\t\t\tend", end, "nextNode:", currentNode)
            print("\t\t\tdistance[end](antes):",distances[end], "distances[nextNode]:",distances[currentNode], "weight:", weight)
            distances[end] = min(distances[end], distances[currentNode] + weight)
            print("\t\t\tdistance[end]:", distances[end])

    return distances

if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    types = list(map(int, input().strip().split()))
    g = [[] for _ in range(n)]
    for _ in range(m):
        c, d, l = map(int, input().strip().split())
        g[c].append((d, l))
        g[d].append((c, l))

    min_distances = [float('inf')] * max(types)
    for i in range(n):
        if types.count(types[i]) > 1:
            print("Iteracion:---------")
            distances = dijkstra(g, i)
            for j in range(n):
                if i != j and types[i] == types[j]:
                    min_distances[types[i]] = min(min_distances[types[i]], distances[j])

    print(' '.join(str(d) if d != float('inf') else '-1' for d in min_distances if d != float('inf')))
