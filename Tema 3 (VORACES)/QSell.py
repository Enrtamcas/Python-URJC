def calculateSed(seduc, currentLove, param1):
    currentLove += seduc


def function(candidates, timeLimit, preference):
    ratio = []
    for candidate in candidates:
        currentPreference = candidate[1][preference]
        currentRatio = currentPreference / candidate[1][3]
        info = [currentRatio, candidate[0], candidate[1][preference], candidate[1][3]]
        ratio.append(info)
    ratio.sort(reverse=True)

    currentTime = 0
    isSol = False
    currentNode = 0
    currentLove = 0
    while currentTime < timeLimit and not isSol:
        currentCandidate = ratio[currentNode]
        timeForCandidate = currentCandidate[3]

        nextTime = currentTime + timeForCandidate
        if nextTime > timeLimit:
            isSol = True
            remainingTime = timeLimit - currentTime
            currentLove += (remainingTime * currentCandidate[2] / timeForCandidate)
        else:
            currentLove += currentCandidate[2]

        currentTime = nextTime
        currentNode += 1
        if currentNode == len(candidates):
            isSol = True
        print(currentCandidate[1], end=' ')
    print()




if __name__ == "__main__":
    n = int(input().strip())

    for _ in range(n):
        c = input().strip()
        preference = 0
        if c == "kindness":
            preference = 2
        elif c == "intelligence":
            preference = 1
        elif c == "beauty":
            preference = 0
        timeLimit = int(input().strip())
        candidates = int(input().strip())
        data = []
        for i in range(candidates):
            o, b, i, k, t = map(str, input().strip().split())
            information = [o, [int(b), int(i), int(k), int(t)]]
            data.append(information)
        function(data, timeLimit, preference)
