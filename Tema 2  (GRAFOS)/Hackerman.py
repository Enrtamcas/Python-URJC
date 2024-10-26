from collections import deque


def isNodeCritic(excluded_node, graph):
    visited = [False] * (len(graph))
    queue = deque()
    current_node = (excluded_node + 1) % len(graph)
    queue.append(current_node)
    visited[current_node] = True

    count = 0
    while queue:
        node_to_expand = queue.popleft()
        if node_to_expand != excluded_node:
            for next_node in graph[node_to_expand]:
                if not visited[next_node]:
                    queue.append(next_node)
                    visited[next_node] = True
                    count += 1
    return count != len(graph) - 1


def calculateCost(graph, graph_cost):
    total_cost = 0
    for current_node in range(len(graph)):
        if isNodeCritic(current_node, graph):
            total_cost += graph_cost[current_node]
    return total_cost


if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    graph = []
    graph_cost = []
    for _ in range(n):
        graph.append([])
        graph_cost.append(int(input().strip()))
    for _ in range(m):
        a, b = map(int, input().strip().split())
        graph[b].append(a)
        graph[a].append(b)

    print(calculateCost(graph, graph_cost))
