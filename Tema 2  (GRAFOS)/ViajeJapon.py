def grafo_profundidad(nodo, grafo, visitado):
    visitado.add(nodo)
    for v in grafo[nodo]:
        if v not in visitado:
            grafo_profundidad(v, grafo, visitado)


if __name__ == '__main__':
    num_ciudades, num_conexiones = map(int, input().strip().split())

    grafo = []
    grafo_inverso = []
    for i in range(num_ciudades):
        grafo.append([])
        grafo_inverso.append([])
    for j in range(num_conexiones):
        a, b = map(int, input().strip().split())
        grafo[a].append(b)
        grafo_inverso[b].append(a)

    ciudades_visitadasG = set()
    ciudades_visitadasIG = set()

    nodo_inicial = 0

    grafo_profundidad(nodo_inicial, grafo, ciudades_visitadasG)
    grafo_profundidad(nodo_inicial, grafo_inverso, ciudades_visitadasIG)

    if len(ciudades_visitadasG) == len(ciudades_visitadasIG):
        print("PERFECTO")
    else:
        print("CAMBIA EL ITINERARIO")
