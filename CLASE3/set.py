from sys import stdin

def set():
	m1=[]
	m2=[]

	auxS=0
	auxG=0
	ans=0

	i=0
	while i<n:

		if sultan[i]<golap[i]:
			m1.append((sultan[i],golap[i]))

		else:
			m2.append((sultan[i],golap[i]))

		i=i+1


	m1.sort(key=lambda x: x[0],reverse=False)
	m2.sort(key=lambda x: x[1],reverse=True)
	

	a=m1+m2


	auxG=0
	auxS=0

	i=0

	while i<n:
		
		auxS=auxS+a[i][0]
		auxG=max(auxS,auxG)+a[i][1]
		
		i=i+1

	print(auxG)


def main():

	global n,sultan,golap
	
	sultan=[8,1,6]
	golap=[1,6,3]
	n=len(sultan)
	set()

"""
def main():

 	global n,sultan,golap

 	linea = stdin.readline()
 	while linea!="":
 		n=int(linea)
 		sultan=[]
 		golap=[]
 		sultan = list(map(int,stdin.readline().split()))
 		golap = list(map(int,stdin.readline().split()))
 		set()
 		linea = stdin.readline()
"""		

main()