#Este código es una adaptación del siguiente video https://www.youtube.com/watch?v=vtJvbRlHqTA&t=219s

from sys import stdin

def maxprodsub(A):

	curr_max_prod = A[0]
	pre_max_prod = A[0]
	pre_min_prod=A[0]
	ans=A[0]

	for i in range(1,len(A)):
		curr_max_prod=max(pre_max_prod*A[i],pre_min_prod*A[i],A[i])
		curr_min_prod=min(pre_max_prod*A[i],pre_min_prod*A[i],A[i])
		ans=max(ans,curr_max_prod)
		pre_max_prod=curr_max_prod
		pre_min_prod=curr_min_prod

	print(ans)
	return ans 

def main():
	np = stdin.readline().strip().split()
	aux=[]
	while np != []:

		for i in np:
			if i =="-999999":
				maxprodsub(aux)
				aux=[]
			else:
				aux.append(int(i))

		np=stdin.readline().strip().split()
	  	
main()

