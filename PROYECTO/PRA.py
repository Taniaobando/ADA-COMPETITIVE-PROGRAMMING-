#Nombre: Tania C. Obando S.
#Codigo: 6036110


"""
Código de Honor 

Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
a seguir los más altos estándares de integridad académica.
Integridad académica se refiere a ser honesto, dar crédito a quien lo merece y respetar el trabajo de los demás. Por eso
es importante evitar plagiar, engañar, ‘hacer trampa’, etc. En particular, el acto de entregar un programa de computador
ajeno como propio constituye un acto de plagio; cambiar el nombre de las variables, agregar o eliminar comentarios
y reorganizar comandos no cambia el hecho de que se está copiando el programa de alguien más.

"""

from sys import stdin


def lights():
	EI=list(bin(int(CI,16))[2:].zfill(K)) #pasar de hexadecimal a binario (Estado inicial)
	
	for i in range(0,M): #en este for recorro todos los estados dados por los m segundos
		ai,bi=lista[i]
		print(ai,"ai original")
		print(bi,"bi original")
		print(k,"K")

		if EI[ai-1] == '0': # si en el extremo izquiendo hay un cero entonces busco el primer uno a la izquirda de ai-1(ai-1 porque inicia en cero)

			if ai-1 !=0: # verifico que el cero no se encuentre en el inicio de la cadena, puesto que ai-2 no existe
				j=ai-2
				while j>=0: #ciclo que busca el primer uno a la izquierda de ai-1 por esto empieza en ai-2
					if EI[j]=='1':
						ai=j
						j=-1
					elif EI[j]=='0' and j==0: #condicion por si no existe un uno despues de que ai-1 es 0
						ai=ai-1
						j=-1
					j=j-1
			else:
				ai=ai-1 #si esta en el extremo le resto 1 a ai porque empieza en cero
		else:
			ai=ai-1	 # si ai-1 es cero y ademas es el inicio de la cadena no deberia buscar el primer 1 a la izquierda solo retarle 1 a ai porque empieza en cero

		if EI[bi-1]=='0': #si en el extremo derecho hay un cero entonces busco el primer uno a la derecha de bi-1
			if bi-1!=K-1: #verifico que el cero no se encuentre al final de la cadena puesto que la posición bi no existe(teniendo en cuenta que empieza en cero)
				z=bi
				while z<=K-1:#ciclo que busca el primer uno a la derecha de bi-1 
					if EI[z]=='1':
						bi=z
						z=K+1
					elif EI[z]=='0' and z==K-1:#condicion por si no existe un uno despues de bi-1
						bi=bi-1
						z=K+1
					
					z=z+1
			else:
				bi=bi-1# si bi-1  es cero y ademas es el final de la cadena no deberia buscar el primero uno a la derecha ya que no existe

		else:
			bi=bi-1 # si bi-1 es uno solo le resto a bi uno porque empieza en cero mi lista
		
		m=ai
		while m<=bi:#ciclo donde algo la negacion de la sub-cadena despues de tener establecido el intervalo que quiero cambiar 

			if EI[m]=='1':
				EI[m]='0'
			else:
				EI[m]='1'
			m=m+1

	EV=''.join(EI)	
	EF=hex(int(EV,2))[2:].upper()#pasar de binario a hexadecimal (Estado final)
	print(EF)



def main():
	global K,M,lista,CI
	tcnt = int(stdin.readline())
	while tcnt!=0:
		K,M=map(int,stdin.readline().split()) # K es el número de bombillos y m el numero de segundos a considerar
		CI= stdin.readline()#Configuración inicial de las luces dada en hexadecimal.
		lista=[]
		for i in range(0,M):
			ai,bi=map(int,stdin.readline().split()) # K es el número de bombillos y m el numero de segundos a considerar
			lista.append((ai,bi))
		lights()
		tcnt=tcnt-1



main()