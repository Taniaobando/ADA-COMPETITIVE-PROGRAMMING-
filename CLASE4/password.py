from sys import stdin

ans=""

def passwords(index):
	global ans
	if index!=len(rules):
		if rules[index]=="#":
			for i in range(len(words)):
				tmp=ans
				ans=ans+words[i]
				passwords(index+1)
				ans=tmp
		else:
			for i in range(10):
				ans=ans+str(i)
				passwords(index+1)
				ans=ans[0:len(ans)-1]
	else:
		print(ans)



words=["root","2super"]
rules="##0"
passwords(0)

"""
def main():

	global cadenas,clave
	cadenas=list()
	ans=""
	line=stdin.readline().strip()

	while line!="":
		nc=int(line)
		while nc!=0:
			tmp=stdin.readline().strip()
			cadenas.append(tmp)
			nc=nc-1

		ncla=int(stdin.readline().strip())
		while ncla !=0:
			clave=stdin.readline().strip()
			passwords(0,ans)
			ncla=ncla-1

		line=stdin.readline().strip()


main()
"""