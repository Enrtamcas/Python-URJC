input_ = input().strip().split()

id_player = input_[0].zfill(3)
color = input_[1]
sensor = int(input_[2])

if color == "r":
    if sensor == 1:
        print("JUGADOR " + id_player + " ELIMINADO")
    else:
        print("JUGADOR " + id_player + " CONTINUAR")
else:
    print("JUGADOR " + id_player + " CONTINUAR")
