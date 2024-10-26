def funcion(data):
    ratio = []
    names = []

    currentCandidate = 0
    for c in data:
        information = data[c]
        place = [information[1] / information[0], information[2], c]
        names.append(c)
        ratio.append(place)
        currentCandidate += 1

    ratio.sort(reverse=True)
    names.sort()

    time = 0
    firstCandidateTime = 0
    for info in ratio:
        print(info[2])
        if info[2] == names[0]:
            firstCandidateTime = time
        time += info[1]

    print(firstCandidateTime)


if __name__ == "__main__":
    n = int(input().strip())

    data = {}
    for i in range(n):
        s, m, l, t = map(str, input().strip().split())
        information = [int(m), int(l), int(t)]
        data[s] = information

    funcion(data)
