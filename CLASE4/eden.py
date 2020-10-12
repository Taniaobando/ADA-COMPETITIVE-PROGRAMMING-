"""
Nombre: Tania C. Obando S.
Codigo: 6036110
Colaboradores: Laura Arango, Juan Camilo Vanegas   

"""

from sys import stdin

def eden(lista,idx,boolu):

	if boolu==0: 

		for i in range(8):
			if clave[i]==estado[idx]:

				aux=matriz[i]

				if idx==lenE-1:
					if lista[idx-1]==aux[0] and lista[idx]==aux[1] and lista[0]==aux[2]:
						boolu=1
					
				elif idx==0:
					lista[0]= aux[1]
					lista[1]=aux[2]
					lista[-1]=aux[0]

					if boolu!=1:
						boolu=eden(lista,idx+1,boolu)
	
				else:
					if lista[idx-1]==aux[0] and lista[idx]==aux[1] and lista[idx+1]==None:
						lista[idx+1]=aux[2]
						boolu=eden(lista,idx+1,boolu)
						lista[idx+1]=None
						
					elif lista[idx-1]==aux[0] and lista[idx]==aux[1] and lista[idx+1]==aux[2] and lista[idx+1]!=None:
						boolu=eden(lista,idx+1,boolu)
	return boolu



def main():
	global matriz,clave,estado,lenE

	matriz=[[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]	
	boolu=0
	booluT=0
	line=stdin.readline().strip().split()
	while len(line) != 0:

		claveT,lenE,estado=int(line[0]),int(line[1]),line[2]

		lista=[None]*lenE
		clave=str(bin(claveT)[2:].zfill(8))

		booluT=eden(lista,0,boolu)
		
		if booluT == 0:
			print("GARDEN OF EDEN")

		else:
			print("REACHABLE")

		line=stdin.readline().strip().split()

main()