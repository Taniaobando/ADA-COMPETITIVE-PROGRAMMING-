from sys import stdin

#basado en la siguiente descripción https://abitofcs.blogspot.com/2014/07/a-bit-of-bitmask-uva-10718-bit-mask.html
#Nombre: Tania C. Obando S.
#Codigo: 6036110

def bitmask(n,l,u):

	N=str(bin(n)[2:].zfill(32))
	L=str(bin(l)[2:].zfill(32))
	U=str(bin(u)[2:].zfill(32))

	m = ""

	bandera1=True
	bandera2=True
	
	i = 0

	while i<32:
		if N[i]=='1':
			if L[i]=='1' and bandera1==True:
				m+='1'
			else:
				m+='0'
				if U[i]=='1':
					bandera2=False
		else:
			if U[i]=='0' and bandera2==True:
				m+='0'
			else:
				m+='1'
				if L[i]=='0':
					bandera1=False
		i+=1

	print(int(m,2))
	return int(m,2)		


def main():
	linea=stdin.readline()
	while linea !="":
		N,L,U=map(int,linea.split())
		bitmask(N,L,U)
		linea=stdin.readline()

main()