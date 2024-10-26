from collections import deque


def laberinth(init, matrix, matrix_visited, target, rows, columns):
    movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    matrix_visited[init[0]][init[1]] = True
    distance = [init, 0]

    queue = deque()
    queue.append(distance)

    while queue:
        current_node, distance_value = queue.popleft()

        if current_node[0] == target[0] and current_node[1] == target[1]:
            return distance_value

        for movement in movements:
            next_node, distance = (current_node[0] + movement[0], current_node[1] + movement[1]), distance_value
            if 0 <= next_node[0] < rows and 0 <= next_node[1] < columns:
                if not (matrix[next_node[0]][next_node[1]] == -1 and distance_value % 2 == 1):
                    if not matrix_visited[next_node[0]][next_node[1]]:
                        matrix_visited[next_node[0]][next_node[1]] = True
                        queue.append([next_node, distance_value + 1])


if __name__ == "__main__":
    rows, columns = map(int, input().strip().split())

    matrix = []
    matrix_visited = []

    target = (0, 0)

    for i in range(rows):
        matrix.append([])
        matrix_visited.append([False] * columns)

    column_counter = 0
    for row in range(rows):
        for value in map(int, input().strip().split()):
            matrix[row].append(value)
            if value == 2:
                target = (row, column_counter)
            column_counter += 1
        column_counter = 0

    print(laberinth((0, 0), matrix, matrix_visited, target, rows, columns))
