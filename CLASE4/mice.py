#Nombre: Tania C. Obando S.
#Codigo: 6036110

from sys import stdin
from heapq import heappop,heappush

INF = float('inf')

def mice(G,ncs,t):
	ans=0
	dist=sssp(G,ncs)

	for k in dist:
		if k <= t:
			ans = ans + 1 
				
	return(ans)


def sssp(G,source): #dijkstra
  """G is a graph representation in adjacency list format with vertices
     in the set { 0, ..., |V|-1 } and source a vertex in G"""
  # dist[u] : "minimum distance detected from source to u
  dist = [ INF for i in range(len(G)) ] ; 
  dist[source] = 0
  visited = [ False for i in range(len(G)) ]
  heap = [ (0,source) ]
  while len(heap)!=0:
    d,u = heappop(heap)
    if not(visited[u]):
      visited[u] = True
      for v,w in G[u]:
        if dist[v]>d+w:
          dist[v] = d+w
          heappush(heap,(dist[v],v))
  return dist


def main():
	  tcnt= int(stdin.readline())
	  espacio1=stdin.readline()
	  while tcnt!=0:
	  	Grafo=[]
	  	nc=int(stdin.readline())#Numero de celdas
	  	ncs=int(stdin.readline())#Numero de la celda de salida
	  	t=int(stdin.readline()) #El valor inicial del temporizador 
	  	m=int(stdin.readline()) #Numero de conexiones en el laberinto 
	  	Grafo = [ list() for _ in range(nc) ] 
	  	
	  	while m!=0:
	  		u,v,d=map(int,stdin.readline().split())
	  		Grafo[v-1].append((u-1,d))
	  		m=m-1
	  	ans=mice(Grafo,ncs-1,t)
	  	espacio2=stdin.readline()
	  	print(ans)
	  	print()
	  	tcnt=tcnt-1

main()