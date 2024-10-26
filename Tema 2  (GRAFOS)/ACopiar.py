from collections import deque


def bfs(node, graph, visited):
    queue = deque()
    visited.add(node)
    queue.append(node)
    while queue:
        node_to_expand = queue.popleft()
        for adjacents in graph[node_to_expand]:
            if adjacents not in visited:
                visited.add(adjacents)
                queue.append(adjacents)


if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    graph = []
    for _ in range(n):
        graph.append([])
    for _ in range(m):
        a, b = map(int, input().strip().split())
        graph[b].append(a)
        graph[a].append(b)

    groups = 0
    visited = set()

    for i in range(n):
        if i not in visited:
            print("DEBUG: " + str(i) + ", " + str(visited))
            bfs(i, graph, visited)
            groups += 1

    print(groups)
