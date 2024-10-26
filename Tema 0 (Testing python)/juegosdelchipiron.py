input_ = input().strip().split()

num = int(input_[0])
goodChar = input_[1]
badChar = input_[2]

for i in range(num):
    for j in range(num):
        if j < (num - 1 - i):
            print(badChar, end='')
        else:
            print(goodChar, end='')
    print()
