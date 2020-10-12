from time import time

INF=1e9

def tsp_db(v,A,vs):
	global memo,n

	if (v,A) in memo:
		ans=memo[(v,A)]
	else:
		ans=INF 
		if A==(1<<n)-1:
			ans=adj[v][vs]
		else:
			for i in range(n):
				if i != v and (A &(1<<i)):
					ans=min(ans,adj[v][i]+tsp_fb(i,(A|(1<<i)),vs))

	
			memo[(v,A)]=ans
	print(ans,"ans")
	return ans

def tsp_fb(v,A,vs):
	global memo,n

	ans=INF 
	if A==(1<<n)-1:
		ans=adj[v][vs]
	else:
		for i in range(n):
			if i != v and (A &(1<<i)):
				ans=min(ans,adj[v][i]+tsp_fb(i,(A|(1<<i)),vs))

	print(ans,"ans")
	return ans



def main():

	global adj,n,memo
	memo=dict()
	n=5
	adj=[	[0,24,13,13,22],
			[24,0,22,13,13],
			[13,22,0,19,14],
			[13,13,19,0,19],
			[22,13,14,19,0]
		]

	s=time()
	ans_fb=tsp_fb(0,1,0)
	f=time()
	print(f-s)
	s=time()
	ans_dp=tsp_db(0,1,0)
	f=time()
	print(f-s)



main()