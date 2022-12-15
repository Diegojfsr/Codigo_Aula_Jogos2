import numpy as np
import time

class Grafo:

    def __init__(self, n):
        self.matriz_adj = np.zeros((n, n), dtype="int")
        self.n_vertices = n

    def imprimir(self):        
        print(self.matriz_adj)

    def inserir_vertice(self, origem, destino, direcao = 0):
        if (direcao == 0): #Não-direcionado
            self.matriz_adj[origem, destino] = 1
            self.matriz_adj[destino, origem] = 1
        else:
            self.matriz_adj[origem, destino] = 1

    def retorna_vizinhos(self, v):
        vizinhos = []
        origem = 0
        while origem < self.n_vertices:
            if self.matriz_adj[origem][v] == 1:
                vizinhos.append(origem)
            origem += 1
        
        return vizinhos

    def conta_componentes(self):
        n_componentes = 0
        visitados = np.zeros(self.n_vertices, dtype="int")
        for v in range(self.n_vertices):
            for w in range(self.n_vertices):
                if self.matriz_adj[v][w] == 1:
                    if visitados[w] == 0:
                        n_componentes += 1
                        self.busca_profundidade(w, visitados)
        
        return n_componentes
                
    def busca_profundidade_grafo(self, v_inicial):
        visitados = np.zeros(self.n_vertices, dtype="int")
        print(visitados)
        self.busca_profundidade(v_inicial, visitados)

    def busca_profundidade(self, v_inicial, visitados):
        visitados[v_inicial] = -1 #Marca como visitado
        for w in range(self.n_vertices):
            valor = self.matriz_adj[v_inicial][w] 
            if (valor == 1): #Verifica se os vértices são vizinhos
                if visitados[w] == 0: #Não visitado
                    print("v{}->w{}".format(v_inicial, w))
                    self.busca_profundidade(w, visitados)

    def verifica_caminho(self, origem, destino):
        linhaori  = origem[0]
        colunaori = origem[1]

        linhadest  = destino[0]
        colunadest = destino[1]

        mapa = self.matriz_adj

        if linhaori == linhadest and \
                colunaori == colunadest:
            mapa[linhaori][colunaori] = 1
            return True
        
        print(np.array(mapa))
        print()
        #tam_lin, tam_col = mapa.shape        
        tam_lin = len(mapa)
        tam_col = len(mapa[0])
        #time.sleep(1)
        
        if (mapa[linhaori][colunaori] == -1):
            #Marca na posição do mapa como visitado
            mapa[linhaori][colunaori] = 1
            
            if (self.verifica_caminho( (linhaori, max(0, colunaori-1) ), destino)):
                return True
            
            if (self.verifica_caminho( (max(0, linhaori-1), colunaori), destino) ):
                return True

            if (self.verifica_caminho( (linhaori, min(tam_col, colunaori+1) ), destino) ):
                return True

            if (self.verifica_caminho( ( min(tam_lin, linhaori+1), colunaori), destino)):
                return True           
            
   
if __name__ == "__main__":
    grafo = Grafo(n=6)

    grafo.matriz_adj = [[0,0, 0, 0, 0, 0, 0, 0], 
                        [0,-1,-1,-1,-1,-1,-1,0],
                        [0,-1,-1,-1,-1,-1,-1,0],
                        [0,-1,-1, 0,-1, 0,-1,0],
                        [0,-1,-1, 0,-1,-1,-1,0],
                        [0, 0,-1, 0,-1,-1,-1,0],
                        [0,-1,-1, 0,-1,-1,-1,0],
                        [0, 0, 0, 0, 0, 0, 0, 0]    
                    ]
    grafo.verifica_caminho( (6,2) , (6,6) )