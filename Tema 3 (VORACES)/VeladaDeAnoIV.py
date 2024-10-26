
def function(data):
    currentTime = 0
    activites = 0
    while data:
        currentActivity = data.pop(0)
        if currentTime < currentActivity[1]:
            activites += 1
            currentTime = currentActivity[0]
    print(activites)


if __name__ == "__main__":
    n = int(input())

    data = []
    for _ in range(n):
        s, i, f = map(str, input().split())
        info = [int(f), int(i), s]
        data.append(info)
    data.sort()
    function(data)