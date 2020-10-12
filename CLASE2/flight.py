import math
from sys import stdin

#Colaboradores: Laura Arango, Veronica Tofiño, Xavier Garzon,Danilo Melgarejo


def flight(a,m):

	ans=0
	INF=float("inf")
	A=a
	M=m

	if (a,m) in diccionario:
		ans=diccionario.get((a,m))

	else:

		if a==9 and m==0:
			ans=0

		elif (m==0 and a!=9):	
			ans=INF
		else:	
			if m!=0 and (0<a<9):
				ans=min(flight(a-1,m-1)+60-matrizW[a-1][m-1],
					flight(a+1,m-1)+20-matrizW[a+1][m-1],
					flight(a,m-1)+30-matrizW[a][m-1])
			elif m!=0 and a==9:
				ans=min(flight(a-1,m-1)+60-matrizW[a-1][m-1],
					flight(a,m-1)+30-matrizW[a][m-1])
			elif m!=0 and a==0:
				ans=min(flight(a+1,m-1)+20-matrizW[a+1][m-1],
					flight(a,m-1)+30-matrizW[a][m-1])

		diccionario[(a,m)]=ans
	
	return ans


def main():

	global matrizW,diccionario
	tcnt= int(stdin.readline())
	while tcnt!=0:
		espacio=stdin.readline()
		millas=int(stdin.readline())//100
		matrizW=[]
		diccionario={}
		altura=9
		i=1
		while i <= 10:
			temp=list(map(int,stdin.readline().split()))
			matrizW.append(temp)
			i=i+1
		result=flight(altura,millas)
		print(result)
		print("")
		tcnt=tcnt-1

main()


