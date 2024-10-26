def sortCandidates(g):
    candidates = []
    for adjs in g:
        for (start, end, weight) in adjs:
            candidates.append((weight, start, end))
    candidates.sort()
    return candidates


def updateComponents(components, new_id, old_id):
    for i in range(len(components)):
        if components[i] == old_id:
            components[i] = new_id


def kruskal(g, efforts):
    candidates = sortCandidates(g)
    components = list(range(len(g)))
    count = len(components) - 1
    sol = 0
    i = 0
    while count > 0 and len(candidates) > i:
        (weight, start, end) = candidates[i]
        if components[start] != components[end]:
            sol += weight
            efforts[start] += weight
            efforts[end] += weight
            count -= 1
            updateComponents(components, components[start], components[end])
        i += 1
    return sol


# Input data
n, m = map(int, input().split())
graph = [[] for _ in range(n)]

# Read relationships and their efforts
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((u, v, w))

# Calculate the effort for each contestant
efforts = [0] * n
total_effort = kruskal(graph, efforts)

# Print the results
for i in range(n):
    print(f"C{i} -> {efforts[i]}")
print(f"Esfuerzo realizado -> {total_effort}")
