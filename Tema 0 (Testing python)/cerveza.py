
quality = int(input())
print(range(quality))

if quality >= 46:
    print("MUY BUENA")
elif quality >= 36:
    print("BUENA")
elif quality >= 21:
    print("REGULAR")
elif quality >=11:
    print("MALA")
elif quality >= 0:
    print("CRUZCAMPO")