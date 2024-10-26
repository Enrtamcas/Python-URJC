from queue import PriorityQueue

def dijkstra(g, origin):
    dist = [float('inf')] * len(g)
    queue = PriorityQueue()

    dist[0] = origin[0]
    queue.put(origin)

    while not queue.empty():
        current_node = queue.get()
        for neighbour in g[current_node[0]]:
            next_dist = dist[current_node[0]] + neighbour[1]
            if next_dist < dist[neighbour[0]]:
                dist[neighbour[0]] = next_dist
                queue.put((neighbour[0], next_dist))
    return dist


if __name__ == "__main__":
    g = []
    n, m, t = map(int, input().strip().split())
    for _ in range(n):
        g.append([])
    for _ in range(m):
        h_1, h_2, d = map(int, input().strip().split())
        g[h_1].append((h_2, d))
        g[h_2].append((h_1, d))

    sol = dijkstra(g, (0,0))
    res = sum(sol)

    if res <= t:
        print(res)
    else:
        print("Aleg, a decorar!")
