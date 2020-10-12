from sys  import stdin


def p(w):
	ans=0
	if w > 0:
		ans+=min(w,200)*2
	if w > 100:
		ans+= (min(w,10000)-100)*3
	if w > 100000:
		ans+=(min(w,1000000)-100000)*5
	if w>1000000:
		ans+= (w-1000000)*7
	return ans

def consumption(A)
	ans=0
	if A<=200:
		ans=A>>1
	elif A<=29900:
		ans=100+(A-200)//3
	elif A<=49799900:
		ans=10000+(A-29900)//5
	else:
		ans=1000000 +(A-49799900)//7
	return(ans)



def solve(A,B):
	cons=consumption(A)
	lo,hi=0,cons+1
	while lo+1 != hi:
		mid=(lo+hi)//2
		if p(cons-mid)-p(mid)==B:
			lo=mid
			hi=lo+1
		if p(cons-mid)-p(mid)<B:
			hi=mid
		else:
			lo=mid
		return p(lo)

def main():
	A,B = map(int,stdin.readline().split())
	#A,B =[int(x) for x in stdin.readline().split()]
	while A+B>0:
		ans=solve(A,B)
		print(ans)
		A,B = map(int,stdin.readline().split())
main()