from sys import stdin 


def subset(x,ans,idx):
	if x==0:
		print(ans)

	elif idx<len(s):
		if arr[idx]>=x:
			subset(x-s[idx],ans+[s[idx]],idx+1)
			subset(x,ans,idx+1)


def main():
	global s,arr
	s=[2,4,4,8,8,9,10,11,12]
	s.sort(reverse=True)
	arr= [None]*len(s)
	arr[-1]=s[-1]
	print(s)
	for i in range(len(s)-2,-1,-1):
		arr[i]=s[i]+arr[i+1]	
	print(arr)
	x=20
	ans=list()
	subset(x,ans,0)

main()
