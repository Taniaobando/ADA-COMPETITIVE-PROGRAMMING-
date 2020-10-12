def knapsack(B,W,n,c):
	ans=None 
	if n==0:

		ans=0
	else:
		ans=knapsack(B,W,n-1,c)
		if W[n-1]<=c:
			ans= max(knapsack(B,W,n-1,c), knapsack(B,W,n-1,c-W[n-1])+B[n-1])

	return ans

def knapsack_tab(B,W,C):
	tab=[[None for _ in range (C+1)] for _ in range(N+1)]
	for i in range(C+1):
		tab[0][c]=0 #llenar la primera columna de ceros 
	
	n,c=1,0
	while n != N+1:
		if c==C+1:
			n,c=n+1,0
		else:
			tab[n][c]=tab[n-1][c]
			if W[n-1]<=c: 
				tab[n][c]=max(tab[n][c],tab[n-1][c-W[n-1]]+B[n-1])
		c+=1
	return tab[N][C]