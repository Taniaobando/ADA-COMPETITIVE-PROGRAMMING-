def ls(A,lena):
	lis,lds=[None for _ in range(lena)],[None for _ in range(lena)] #se puede inicializar como listas vacias

	bestlis,bestlds=0,0

	for n in range(lena):
		lis[n]=lds[n]=1
		for i in range(n):
			if A[i]<=A[n] and lis[i]>=lis[n]: lis[n]=lis[i]+1
			#if A[i]<=A[n] : lis[n] = max(lis[n],lis[i]+1)
			if A[i]>=A[n] and lds[i]>=lds[n]: lds[n]=lds[i]+1

		bestlis,bestlds=max(bestlis,lis[n]), max(bestlds,lds[n])
	print("lis:",max(lis))
	print("lds:", max(lds))

	return(max(lis),max(lds))


def main():
	A=[10,3,0,8,2,4,1,6,7,-2,11]

	ls(A,len(A))

main()