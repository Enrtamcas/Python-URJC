def isSol(bag, currentCost, objects, total_cost):
    min_cost = 0x3f3f3f
    #min_cost = float('inf')
    for obj in objects:
        if obj not in bag and min_cost > obj[1]:
            min_cost = obj[1]
    next_cost = currentCost + min_cost
    return next_cost > total_cost


def isFactible(currentCost, object, selected, total_cost):
    next_cost = currentCost + object[1]
    return (next_cost <= total_cost) and (object not in selected)


def function(currentBag, objects, currentCost, currentProfit, selected, bestCost, bestProfit, bestBag, x, total_cost):
    if isSol(currentBag, currentCost, objects, total_cost):
        if currentProfit > bestProfit:
            bestProfit = currentProfit
            bestCost = currentCost
            bestBag = currentBag.copy()
        return bestCost, bestProfit, bestBag
    else:
        for k in range(x, len(objects)):
            obj = objects[k]
            if isFactible(currentCost, obj, selected, total_cost):
                currentBag.append(obj)
                currentCost += obj[1]
                currentProfit += obj[2]
                selected.add(obj)
                bestCost, bestProfit, bestBag = function(currentBag, objects, currentCost, currentProfit,
                                                         selected, bestCost, bestProfit, bestBag, k + 1, total_cost)
                currentBag.pop()
                currentCost -= obj[1]
                currentProfit -= obj[2]
                selected.remove(obj)
    return bestCost, bestProfit, bestBag


if __name__ == "__main__":
    n, P, B = map(int, input().strip().split())
    objects = []
    for _ in range(n):
        o, c, g = map(str, input().strip().split())
        objects.append((o, int(c), int(g)))

    bag = []
    selected = set()
    bestCost, bestProfit, bestBag = function(bag, objects, 0, 0, selected, 0, 0, bag, 0, P)
    bestBag.sort()

    for obj in bestBag:
        print(obj[0], end=" ")
    print()
    print(bestCost, bestProfit)

    if bestProfit <= B:
        print("VUELVE")
    else:
        print("SE VA")