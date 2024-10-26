from queue import PriorityQueue

def dijkstra(g, start, end):
    n = len(g)
    dist = [float('inf')] * n
    prev = [None] * n
    queue = PriorityQueue()
    queue.put((0, start))
    dist[start] = 0

    while not queue.empty():
        current_node = queue.get()
        for next_node in g[current_node[1]]:
            next_dist = dist[current_node[1]] + next_node[1]
            if next_dist < dist[next_node[0]]:
                dist[next_node[0]] = next_dist
                prev[next_node[0]] = current_node[1]
                queue.put((next_dist, next_node[0]))
    path = []
    print(prev)
    while end is not None:
        path.append(end)
        end = prev[end]
    path.reverse()
    print(path)
    return dist, path


if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    g = []
    for _ in range(n):
        g.append([])
    for _ in range(m):
        c1, c2, d = map(int, input().strip().split())
        g[c1].append((c2, d))
        g[c2].append((c1, d))
    s, e = map(int, input().strip().split())
    dist, path = dijkstra(g, s, e)

    print(dist[e])
    string = ""
    for p in path:
        string += str(p) + " "
    string = string[:-1]
    print(string)