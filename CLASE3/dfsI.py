#DFS ITERATIVA 
"""
busqueda en profundidad

"""
def dfs(G,s): 
	N= len(G)
	visited=[0 for _ in G]
	stack=[s]; visited[s]=1
	while len(stack)!=0:
		u=stack.pop()
		assert visited[u]==1
		for v in G[u]:
			if visited[v]==0:
				stack.append(v); visited[v]=1
		visited[u]=2
		return visited

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

print(dfs(G,5))


