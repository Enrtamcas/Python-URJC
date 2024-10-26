from collections import deque


def expandNodes(v, graph, nodesToExpand, visited):
    newNodes = []
    for current_node in nodesToExpand:
        for adj in graph[current_node]:
            if adj not in visited:
                newNodes.append(adj)
                visited.add(adj)
    return newNodes


def bfs(v, graph, level, visited):
    visited.add(v)
    current_level = 0

    nodesToExpand = deque()
    nodesToExpand.append(v)

    while current_level < level - 1:
        nodesToExpand = expandNodes(v, graph, nodesToExpand, visited)
        current_level += 1
    return len(visited)


def calculateFans(graph, level):
    visited = set()
    bfs(0, graph, level, visited)
    return len(visited)


if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        m, k, c = map(int, input().strip().split())
        g = []

        for i in range(k):
            g.append([])
        for j in range(c):
            a, b = map(int, input().strip().split())
            g[a].append(b)
            g[b].append(a)
        print(calculateFans(g, m))
