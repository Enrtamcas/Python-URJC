def es_palindromo(palabra):
    return palabra == palabra[::-1]

num = int(input().strip())
firstLost = -1

ana_puntos = 0
monica_puntos = 0

for i in range(num):
    palabra = input().strip()
    if es_palindromo(palabra):
        if i % 2 == 0:  # Si el índice es par, es el turno de Ana
            ana_puntos += 1
        else:  # Si el índice es impar, es el turno de Mónica
            monica_puntos += 1
    else:
        if firstLost == -1:
            if i % 2 == 0:  # Si el índice es par, es el turno de Ana
                firstLost = 0
            else:
                firstLost = 1


resultado = str(ana_puntos) + " " + str(monica_puntos) + " "

if firstLost == 1:
    resultado += "ANA"
elif firstLost == 0:
    resultado += "MONICA"
else:
    resultado += "EMPATE"

print(resultado)
