from sys import stdin



def train(A,lena):
	lis,lds=[None for _ in range(lena)],[None for _ in range(lena)] #se puede inicializar como listas vacias

	bestlis,bestlds=0,0
	temp=-1

	for n in range(lena):
		lis[n]=lds[n]=1
		for i in range(n):
			if A[i]<=A[n] and lis[i]>=lis[n]: lis[n]=lis[i]+1
			#if A[i]<=A[n] : lis[n] = max(lis[n],lis[i]+1)
			if A[i]>=A[n] and lds[i]>=lds[n]: lds[n]=lds[i]+1

		temp=max((lis[n]+lds[n])-1,temp)
		#bestlis,bestlds=max(bestlis,lis[n]), max(bestlds,lds[n])
	print(temp)
	return(temp)
"""
def main():
	A=[5774, 14874, 11070, 21745, 18117, 7421, 6304, 14248, 4906, 18443, 21314, 18897, 10878, 24586, 20905, 10565, 16532, 2226, 14547, 18180, 22778, 625, 5367, 1945, 77, 4555, 19333, 7223, 4200, 10104, 14850, 10528, 18098, 21653]
	#A=[10,3,0,8]
	train(A,len(A))

"""
def main():
	i=1
	tcnt = int(stdin.readline())
	while tcnt!=0:
		lista=[]
		i=1
		ans=None
		n = int(stdin.readline())
		while i <= n:
			lista.append(int(stdin.readline()))
			i=i+1
		ans=train(lista[::-1],n)#::-1 voltea el arreglo 
		tcnt -= 1

main()