
def conflict(A,n,i):
	ans,j =False,0
	while ans==False and  j!=n:
		ans,j=A[j]==i or n-j==i-A[j] or n-j==A[j]-i,j+1
		#ans,j=A[j]==i or n-j==abs(i-A[j]), j+1
	return ans 

def solve2(A,n,alll):
	if n==8:  
		alll.append(list(A))
	else:
		if A[n]!=None:
			if conflict(A,n,A[n])==False:
				solve2(A,n+1,alll)
		else:

			for i in range(8):
				if  conflict(A,n,i)==False:
					A[n]=i
					solve2(A,n+1,alll)
					A[n]=None
	return alll

	
A=[6,2,7,1,4,0,5,3]
sols=list()
print(solve2(A,0,sols))



"""
def bruteforce(A,n):
	if n==8:
		if  conflict2(A):
			print(A)
		else: 
			for u in range(8)
				A[n]=i
				solve(A,n+1)
"""

"""
def solve(A,n,alll):
	if n==8:  
		alll.append(list(A))
	else:
		for i in range(8):
			if  conflict(A,n,i)==False:
				A[n]=i
				solve(A,n+1,alll)
	return alll


A=[None]*8
sols=list()
print(len(solve(A,0,sols)))
"""
