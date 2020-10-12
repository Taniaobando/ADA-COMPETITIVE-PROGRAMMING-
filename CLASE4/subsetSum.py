from sys import stdin 


def subset(x,ans,idx):
	if x==0:
		print(ans)
	elif idx<len(s):
		if x-s[idx]>=0:
			subset(x-s[idx],ans+[s[idx]],idx+1)
			subset(x,ans,idx+1)

def main():
	global s,x
	s=[2,4,4,8,8,9,10,11,12]
	

	x=20
	ans=list()
	subset(x,ans,0)

main()
