"""
Busqueda en amplitud
"""
from collections import deque 


def bfs(G,s):

	N=len(G)
	visited=[0 for _ in G]
	queue=deque(); queue.append(s);visited[s]=1
	dist=[float('inf') for _ in G]; dist[s]=0
	while len(queue)!=0:
		u=queue.popleft()
		assert visited[u]==1
		for v in G[u]:
			if visited[v]==0:
				queue.append(v); visited[v]=1
				dist[v]=dist[u]+1
		visited[u]=2
	return list(zip(visited,dist))



G=[
	[1],
	[0,2,6,3],
	[1,3],
	[1,2,4],
	[5,3],
	[4,7,6],
	[1,5],
	[5],
	[],

	]

print(bfs(G,5))