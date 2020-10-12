# a = filas
# b = columnas 
# c=horas restantes 
import math
from sys import stdin

def term(a,e,h):

	INF = -float('inf')
	ans=0

	if (a,h) in diccionario:
		ans=diccionario.get((a,h))
	else:
		if a!=0 and e==0:
			ans= INF
		elif a!=0 and e!=0 and L[a-1][e-1]<5:
			ans=term(a,e-1,h)
		elif a!=0 and e!=0 and L[a-1][e-1] >= 5 and h<e:
			ans=term(a,e-1,h)
		elif a!=0 and e!=0 and L[a-1][e-1]>=5  and h>=e:
			nolatomo=term(a,e-1,h)
			latomo=term(a-1,E,h-e)+L[a-1][e-1]
			ans=max(nolatomo,latomo)

		diccionario[(a,h)]=ans 

	return(ans)


def main():
	global L,E,diccionario
	i=1
	tcnt = int(stdin.readline())
	while tcnt!=0:
		diccionario={}
		ans=None
		temp=0
		L=[]
		i=1
		a,e = map(int,stdin.readline().split())
		E=e
		h=e
		A=a
		while i <= a:
			L.append(list(map(int,stdin.readline().split())))
			i=i+1
		ans=term(a,e,h)
		temp= ans/A
		if  str(temp)=="-inf":
			print("Peter, you shouldn't have played billiard that much.")
		else:
			print("Maximal possible average mark - {0:.2f}.".format(temp))

		tcnt -= 1

main()