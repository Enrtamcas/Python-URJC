from collections import deque


def bfs(g, dependecies):
    queue = deque()
    for i in range(len(g)):
        if dependecies[i] == 0:
            queue.append(i)

    orden = []

    while queue:
        comic = min(queue)
        queue.remove(comic)
        orden.append(comic)

        for next_comic in g[comic]:
            dependecies[next_comic] -= 1
            if dependecies[next_comic] == 0:
                queue.append(next_comic)
    return orden


if __name__ == "__main__":
    n, m = map(int, input().strip().split())

    g = []

    for _ in range(n):
        g.append([])

    in_grafo = [0] * n

    for _ in range(m):
        a, b = map(int, input().strip().split())
        g[a].append(b)
        in_grafo[b] += 1

    sortedList = bfs(g, in_grafo)
    string = ""
    for i in sortedList:
        string += str(i) + " "
    string = string[:-1]
    print(string)
