
def conflict(T,r,c,v): #tablero,fila,columna,valor
	ans=False
	while ans==False and i !=9:
		if i!=c: ans=T[r][i]==V
		if i!=r: ans=ans or T[i][c]==V

		i += 1
	i,rr,cc=0,(r//3)*3,(c//3)*3
	while ans==False and i!=3:
		j=0
		while ans==False and j!=3:
			if (rr+i,cc+j) != (r,c):
				ans=T[rr+i][cc+j]==v
			j+=1
		i+=1	
	return ans



def solve(T,r,c):

	ans=None
	if r==9:
		ans=True
	else:
		if c==9:
			ans=solve(T,r+1,0)
		else:
			if T[r][c]!=None:
				if conflict(T,r,c,T[r][c])==False:
					ans=solve(T,r,c+1)
				else:
					ans=False
			else:
				ans,v=False,1
				while ans==False and v!=10:
					if conflict(T,r,c,v)==False:
						T[r][c]=v
						ans=solve(T,r,c+1)
					v +=1
	return ans


def main():

	t=[[None,None,None,6,None,None,4,8,9],
		[6,4,None,None,None,None,None,5,None],
		[None,2,None,None,4,None,None,None,None],
		[None,None,None,None,None,5,8,None,3],
		[1,8,None,None,None,None,9,2,4],
		[None,None,None,6,None,None,None,None,None],
		[None,None,None,6,None,None,None,None,None],
		[None,None,None,6,None,None,None,None,None],
		[None,None,None,6,None,None,None,None,None],
		]

main()
