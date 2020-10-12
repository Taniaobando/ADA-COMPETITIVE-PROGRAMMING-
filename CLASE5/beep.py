#Nombre: Tania C. Obando S.
#Codigo: 6036110

from sys import stdin
from time import time

INF=1e9

def tsp_dp(v, A, vs):
  global memo
  ans = INF
  if (v,A) in memo:
    ans = memo[(v,A)]
  else:
    if A == (1<<n) - 1:
      ans = adj[v][vs]
    else:
      for i in range(n):
        if i != v and (A & (1<<i)) == 0:
          ans = min(ans, adj[v][i] + tsp_dp(i, (A | (1<<i)), vs))
    memo[(v,A)] = ans
  return ans


def main():
	global adj,n,memo

	tcnt=int(stdin.readline().strip())
	while tcnt!=0:
		lista=[]
		filas,columnas=map(int,stdin.readline().split())
		tmp1=list(map(int,stdin.readline().split()))
		lista.append(tmp1)
		BP=int(stdin.readline().strip())
		adj=[[0 for _ in range(BP+1)] for _ in range(BP+1)]
		aux=BP
		ans=0
		memo=dict()
		n=BP+1

		while aux!=0:
			tupla=list(map(int,stdin.readline().split()))
			lista.append(tupla)
			aux=aux-1
		

		for i in range(0,n):
			for j in range(0,n):
				if i!=j:
					adj[i][j]=(abs(lista[i][0]-lista[j][0])+abs(lista[i][1]-lista[j][1]))
		
		ans=tsp_dp(0,0,0)
		print("The shortest path has length",ans)
		tcnt=tcnt-1


main()