from sys import stdin
INF = -float('inf')
def cut_rod(p,n):
	ans = 0
	if n > 0:
		ans = -float('inf')
		for i in range (1,n +1):
			ans = max (ans, p[i] + cut_rod(p,n-i))
	return ans
def memo_cut_rod(p,n,r):
	ans = 0
	if r[n] > 0: 
		ans = r[0]
	else:
		q = -float('inf')
		for i in range (1,n + 1):
			ans = max(ans,p[i] + memo_cut_rod(p,n-i,r))
		r[n]=ans
	return ans

def tab_cut_rod(p,n):
	r = [INF for i in range (n+1)]
	r[0]=0
	for i in range (1,n+1):
		q = p[i]
		for j in range (1,i):
			q = max(q,p[j]+r[i-j])
		r[i]=q
	return r[n]

def main():
	n = int(stdin.readline())
	p = list()
	p.append(0)
	for i in range(n):
		x = int(stdin.readline())
		p.append(x)
	s0 = time.time()
	cut_rod(p,n)
	s1 = time.time()
	print(s1-s0)
	
	s0 = time.time()
	r=[INF for _ in range (n+1)]
	memo_cut_rod(p,n,r)
	s1=time.time()
	print(s1-s0)

	s0= time.time()
	tab_cut_rod(p,n)
	s1 = time.time()
	print(s1-s0)


