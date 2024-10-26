input_ = input().strip().split()

map = {}
target = []
continueToReadList = True

contador = 0
while continueToReadList:
    value = int(input_[contador])
    if value != -1:
        map[value] = map.get(value, 0) + 1
        contador = contador + 1
    else:
        continueToReadList = False


for n in map.keys():
    if map[n] >= 3:
        target.append(n)

target.sort()
string = ""
for printTarget in target:
    string = string + str(printTarget) + " "
string = string[:-1]
print(string)


