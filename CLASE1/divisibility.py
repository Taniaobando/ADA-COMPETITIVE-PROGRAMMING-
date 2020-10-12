from sys import stdin,setrecursionlimit
setrecursionlimit(11000)



def solve(A,n,K,m):
	ans=None
	if n==0:
		ans=(m==0)
	else:
		if (n,m) in diccionario:
			ans=diccionario.get((n,m))
		else:
			ans=solve(A,n-1,K,(m+A[n-1])%K) or solve(A,n-1,K,(m-A[n-1])%K)
			diccionario[(n,m)]=ans
	return(ans)


def main():
 	global diccionario
 	tcnt = int(stdin.readline())
 	while tcnt!=0:
	  	ans=None
	  	diccionario={}
	  	N,K = map(int,stdin.readline().split())
	  	num = list(map(int,stdin.readline().split()))
	  	m=0
	  	ans=solve(num,N,K,m)

	  	print('Divisible' if ans else 'Not divisible')
	  	tcnt -= 1
"""
def main():

	num=[24369, 1793, 51546, 44696, 87959, 15876, 70870, -4291, 95581, 29777, 29662, 57322, 74030, 86733, 67227, 81441, 8627, 61786, 6210, 96764, 12804, 89070, 90863, 66912, 81203, -3044, 94419, 69065, 34678, 65169, 30282, 18039, 90156]
	m=0
	N=33
	K=98
	print('Divisible' if solve(num,N,K,m) else 'Not divisible')
"""
main()
