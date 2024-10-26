def returnExpandedList(graph, visited, nodesToExpand):
    newNodos = []
    for current_node in nodesToExpand:
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                newNodos.append(neighbor)
                visited.append(neighbor)
    return newNodos


def bfs(v, graph, level, max):
    nodes_to_expandand = [v]
    visited = [v]
    current_level = level

    if max == 0:
        return 1

    while current_level < max:
        nodes_to_expandand = returnExpandedList(graph, visited, nodes_to_expandand)
        current_level += 1

    return len(visited)


def calculateFans(graph, m):
    k = m - 1
    return bfs(0, graph, 0, k)


if __name__ == '__main__':
    n = int(input().strip())
    list = []

    for _ in range(n):
        m, k, c = map(int, input().strip().split())

        g = []
        for _ in range(k):
            g.append([])
        for _ in range(c):
            a, b = map(int, input().strip().split())
            g[a].append(b)
            g[b].append(a)

        list.append(calculateFans(g, m))

    for printedObject in list:
        print(printedObject)
