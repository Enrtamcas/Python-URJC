def selectMinNode(distance, visited):
    min_dist = float('inf')
    min_node = -1
    for node in range(len(distance)):
        if not visited[node] and distance[node] < min_dist:
            min_dist = distance[node]
            min_node = node
    return min_node


def dijkstra(g, start):
    n = len(g)

    visited = [False] * n
    distance = [float("inf")] * n

    visited[start] = True
    distance[start] = 0

    for nextNode in g[start]:
        end, weight = nextNode
        if weight < distance[end]:
            distance[end] = weight

    for i in range(n):
        currentNode = selectMinNode(distance, visited)
        visited[currentNode] = True
        for nextNode in g[currentNode]:
            end, weight = nextNode
            nextDistance = distance[currentNode] + weight
            if nextDistance < distance[end]:
                distance[end] = nextDistance
    return distance


if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    g = [[] for i in range(n)]

    for _ in range(m):
        s, e, w = map(int, input().strip().split())
        g[s].append((e, w))
        g[e].append((s, w))

    origin = 0
    print(dijkstra(g, origin))
