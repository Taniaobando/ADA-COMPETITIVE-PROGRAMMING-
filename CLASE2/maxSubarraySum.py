#version con arrglo

def msa(A):
	N=len(A)
	msa=[None for _ in range(N)]
	ans=0
	if N!=0:
		msa[0]=A[0]
	for n in range(1,N):
		msa[n]=max(msa[n-1]+A[n],A[n])
		ans=max(ans,msa[n])
	print(max(ans,0))
	return max(ans,0)


def msa_opt(A):
	N,ans=len(A),0
	if N!=0:
		lastsum=A[0]
		for n in range(1,N):
			lastsum=max(lastsum+A[n],A[n])
			ans=max(ans,lastsum)
	print("msa_opt:",max(ans,0))
	return max(ans,0)

def main():
	A=[3,-2,6,-5,5,1,-2,-3]
	msa(A)
	msa_opt(A)



main()
#version con una sola variables 