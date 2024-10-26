if __name__ == "__main__":
    n = int(input().strip())

    tree = [0] * n
    asigned = [False] * n

    root = 1
    for _ in range(n):
        it = 0
        descends = list(map(int, input().strip().split()))
        for member in descends:
            if it == 0:
                father = member
                if not asigned[father]:
                    tree[father] = root
                    asigned[father] = True
            else:
                tree[member] = tree[father] + 1
                asigned[member] = True
            it += 1

    n = int(input().strip())

    for _ in range(n):
        print(tree[int(input().strip())])
