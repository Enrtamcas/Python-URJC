def selectMinNode(distances, visited):
    min_distance = float('inf')
    min_index = -1
    for j in range(len(distances)):
        if not visited[j] and distances[j] < min_distance:
            min_distance = distances[j]
            min_index = j
    return min_index


def dijkstra(g, origin, final):
    n = len(g)
    path = []
    prev = [None] * n
    visited = [False] * n
    distances = [float('inf')] * n
    distances[origin] = 0
    visited[origin] = True

    for end, weight in g[origin]:
        if weight < distances[end]:
            distances[end] = weight
            prev[end] = origin

    for i in range(n):
        currentNode = selectMinNode(distances, visited)
        visited[currentNode] = True
        for nextNode in g[currentNode]:
            end, weight = nextNode
            nextDistance = distances[currentNode] + weight
            if nextDistance < distances[end]:
                distances[end] = nextDistance
                prev[end] = currentNode

    while final is not None:
        path.append(final)
        final = prev[final]
    path.reverse()
    print(path)

    return distances


if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    g = [[] for i in range(n)]

    for _ in range(m):
        s, e, w = map(int, input().strip().split())
        g[s].append((e, w))
        g[e].append((s, w))


    start, end = map(int, input().strip().split())
    print(dijkstra(g, start, end))
