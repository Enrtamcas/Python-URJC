if __name__ == "__main__":
    n, m = map(int, input().split())
    types = list(map(int, input().strip().split()))

    g = [[] for i in range(n)]
    for i in range(m):
        c, d, l = map(int, input().strip().split())
