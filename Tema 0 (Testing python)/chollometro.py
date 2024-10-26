n = input().strip().split()

id = 1
maxId = 0
max = 0

for i in n:
    if (int(i) > max):
        max = int(i)
        maxId = id

    string = str(id) + " "
    for equals in range(0, int(i)):
        string = string + "="
    print(string)
    id = id + 1

print("El mas usado es el cupon " + str(maxId) + " con " + str(max) + " usos")
