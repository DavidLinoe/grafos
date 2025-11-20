from collections import deque

def criar_grafo():
    return {}

def inserir_vertice(grafo, vertice):
    if vertice not in grafo:
        grafo[vertice] = []

def inserir_aresta(grafo, origem, destino, nao_direcionado=False):
    inserir_vertice(grafo, origem)
    inserir_vertice(grafo, destino)
    if destino not in grafo[origem]:
        grafo[origem].append(destino)
    if nao_direcionado and origem not in grafo[destino]:
        grafo[destino].append(origem)

def remover_vertice(grafo, vertice):
    if vertice in grafo:
        del grafo[vertice]
    for v in grafo:
        if vertice in grafo[v]:
            grafo[v].remove(vertice)

def remover_aresta(grafo, origem, destino, nao_direcionado=False):
    if origem in grafo and destino in grafo[origem]:
        grafo[origem].remove(destino)
    if nao_direcionado and destino in grafo and origem in grafo[destino]:
        grafo[destino].remove(origem)

def exibir_grafo(grafo):
    for v in grafo:
        print(f"{v} -> {grafo[v]}")

def vizinhos(grafo, vertice):
    return grafo.get(vertice, [])

def existe_aresta(grafo, origem, destino):
    return origem in grafo and destino in grafo[origem]


# -------- BFS --------

def busca_em_largura(grafo, inicio):
    if inicio not in grafo:
        return []
    visitado = set([inicio])
    fila = deque([inicio])
    ordem = []
    while fila:
        v = fila.popleft()
        ordem.append(v)
        for w in grafo[v]:
            if w not in visitado:
                visitado.add(w)
                fila.append(w)
    return ordem

def busca_menor_caminho_bfs(grafo, origem, destino):
    if origem not in grafo or destino not in grafo:
        return []
    visitado = set([origem])
    fila = deque([origem])
    pai = {origem: None}
    while fila:
        v = fila.popleft()
        for w in grafo[v]:
            if w not in visitado:
                visitado.add(w)
                pai[w] = v
                if w == destino:
                    caminho = []
                    while w is not None:
                        caminho.append(w)
                        w = pai[w]
                    return caminho[::-1]
                fila.append(w)
    return []


# -------- DFS --------

def dfs(grafo, inicio):
    if inicio not in grafo:
        return []
    visitado = set()
    ordem = []
    def visitar(v):
        visitado.add(v)
        ordem.append(v)
        for w in grafo[v]:
            if w not in visitado:
                visitar(w)
    visitar(inicio)
    return ordem

def dfs_detecta_ciclo(grafo):
    visitado = set()
    pilha = set()

    def visitar(v):
        visitado.add(v)
        pilha.add(v)
        for w in grafo[v]:
            if w not in visitado:
                if visitar(w):
                    return True
            elif w in pilha:
                return True
        pilha.remove(v)
        return False

    for v in grafo:
        if v not in visitado:
            if visitar(v):
                return True
    return False


# -------- MENU --------

def main():
    grafo = criar_grafo()
    while True:
        print("\n1-Mostrar  2-Vertice  3-Aresta  4-RemoverV  5-RemoverA")
        print("6-Vizinhos  7-Aresta?  8-BFS  9-MenorCaminho")
        print("10-DFS  11-Ciclo?  0-Sair")
        op = input("Opção: ")

        if op == '1':
            exibir_grafo(grafo)

        elif op == '2':
            inserir_vertice(grafo, input("Vértice: "))

        elif op == '3':
            o = input("Origem: "); d = input("Destino: ")
            inserir_aresta(grafo, o, d, input("Não direcionado? (s/n): ").lower() == 's')

        elif op == '4':
            remover_vertice(grafo, input("Vértice: "))

        elif op == '5':
            o = input("Origem: "); d = input("Destino: ")
            remover_aresta(grafo, o, d, input("Não direcionado? (s/n): ").lower() == 's')

        elif op == '6':
            print("Vizinhos:", vizinhos(grafo, input("Vértice: ")))

        elif op == '7':
            o = input("Origem: "); d = input("Destino: ")
            print("Existe?" if existe_aresta(grafo, o, d) else "Não existe")

        elif op == '8':
            i = input("Início BFS: ")
            print("BFS:", " -> ".join(busca_em_largura(grafo, i)))

        elif op == '9':
            o = input("Origem: "); d = input("Destino: ")
            c = busca_menor_caminho_bfs(grafo, o, d)
            print("Menor caminho:", " -> ".join(c) if c else "Inexistente")

        elif op == '10':
            i = input("Início DFS: ")
            print("DFS:", " -> ".join(dfs(grafo, i)))

        elif op == '11':
            print("Ciclo encontrado" if dfs_detecta_ciclo(grafo) else "Sem ciclo")

        elif op == '0':
            break

if __name__ == "__main__":
    main()
