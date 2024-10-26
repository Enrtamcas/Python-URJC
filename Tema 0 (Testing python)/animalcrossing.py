# entrada = int(input().strip())

n = int(input())

mxID = [0, 0]
mxPZ = [0, 0]

for(n) in range (0, n):
    id, pez = map(int, input().strip().split())
    if pez > mxPZ[0]:
        antPZ = mxPZ[0]
        antID = mxID[0]
        mxPZ[0] = pez
        mxID[0] = id
        mxPZ[1] = antPZ
        mxID[1] = antID
    elif pez > mxPZ[1]:
        mxPZ[1] = pez
        mxID[1] = id


suma = mxPZ[0] + mxPZ[1]
print(mxID[0],mxID[1],suma)




