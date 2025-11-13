
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

def exibir_grafo(grafo):
    for v in grafo:
        print(f"{v} -> {grafo[v]}")

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

def vizinhos(grafo, vertice):
    return grafo.get(vertice, [])

def existe_aresta(grafo, origem, destino):
    return origem in grafo and destino in grafo[origem]

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

def main():
    grafo = criar_grafo()
    while True:
        print("\n1-Mostrar  2-Vertice  3-Aresta  4-RemoverV  5-RemoverA  6-Vizinhos  7-Aresta?  8-BFS  9-MenorCaminho  0-Sair")
        op = input("Opção: ")
        if op == '1':
            exibir_grafo(grafo)
        elif op == '2':
            inserir_vertice(grafo, input("Vértice: "))
        elif op == '3':
            origem = input("Origem: "); destino = input("Destino: ")
            inserir_aresta(grafo, origem, destino, input("Não direcionado? (s/n): ").lower() == 's')
        elif op == '4':
            remover_vertice(grafo, input("Vértice: "))
        elif op == '5':
            origem = input("Origem: "); destino = input("Destino: ")
            remover_aresta(grafo, origem, destino, input("Não direcionado? (s/n): ").lower() == 's')
        elif op == '6':
            v = input("Vértice: "); print("Vizinhos:", vizinhos(grafo, v))
        elif op == '7':
            o = input("Origem: "); d = input("Destino: ")
            print("Existe?" if existe_aresta(grafo, o, d) else "Não existe")
        elif op == '8':
            i = input("Início: "); print("BFS:", " -> ".join(busca_em_largura(grafo, i)))
        elif op == '9':
            o = input("Origem: "); d = input("Destino: ")
            c = busca_menor_caminho_bfs(grafo, o, d)
            print("Menor caminho:", " -> ".join(c) if c else "Inexistente")
        elif op == '0':
            break

if __name__ == "__main__":
    main()
