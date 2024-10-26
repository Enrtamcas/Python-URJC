def selectMinNode(visited, distances):
    min_distance = float('inf')
    min_node = -1
    for i in range(len(visited)):
        if not visited[i] and distances[i] < min_distance:
            min_distance = distances[i]
            min_node = i
    return min_node


def dijkstra(graph, origin):
    n = len(graph)
    visited = [False] * n
    distances = [float('inf')] * n
    visited[origin] = True
    distances[origin] = 0

    for node in graph[origin]:
        weight, end = node
        if weight < distances[end]:
            distances[end] = weight

    for i in range(n):
        currentNode = selectMinNode(visited, distances)
        visited[currentNode] = True
        for end, weight in graph[currentNode]:
            if weight < distances[end]:
                distances[end] = weight
    return distances
