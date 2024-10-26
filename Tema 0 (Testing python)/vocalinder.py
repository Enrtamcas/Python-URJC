num = int(input())
user = input()

user_listed = list(user)
user_vocals = 0
vocal_list = list("aeiouAEIOUáéíóúÁÉÍÓÚ")

for n in user_listed:
    for nv in vocal_list:
        if n == nv:
            user_vocals += 1

for i in range(num):
    name = input()
    name_listed = list(name)
    name_vocals = 0
    for j in name_listed:
        for jv in vocal_list:
            if j == jv:
                name_vocals += 1
    if name_vocals == user_vocals:
        print("ITS A MATCH!")
    else:
        print("NEXT!")