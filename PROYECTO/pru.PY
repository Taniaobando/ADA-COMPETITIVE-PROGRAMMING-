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

def encontrarUnoAi(a,EI): #Funcion que encuentra el uno del extremo izquiendo
	partea=(EI>>(k-a+1)) #Saca la parte desde 0 hasta ai-1
	uno1=(partea&-partea).bit_length()-1 #devuelve la posición del uno más  a la izquierda de ai 
	if uno1==-1: #si devuelve -1 no hay ningun uno en la parte a
		ai=uno1

	else:
		ai=(k-1)-(uno1+(k-a+1)) #transforma la posicion del uno encontrado en la parte a en terminos de las posiciones de la cadena EI

	return (ai)

def encontrarUnoBi(b,EI):#Funcion que encuntra el uno del extremo derecho
	AUX=1
	AUX=(AUX<<(k-b))
	AUX=AUX-1
	parteb=(EI&AUX) #Saca la parte desde bi+1 hasta K
	uno2=parteb.bit_length()-1 #devuelve la posición del uno mas a la derecha de bi 
	if uno2==-1:#devuelve -1 en caso de no encontrar un uno
		bi=uno2 
	else:
		bi=(k-uno2-1)#transforma la posicion del uno encontrado en la parte b en terminos de las posiciones de la cadena EI
		
	return (bi)


def negarCadena(ai,bi,EI):#Función que niega desde el limite ai hasta bi dado un número decimal EI que representa una cadena binaria
	"""
	pone unos en las posiciones que quiren ser cambiadas y ceros en las que no luego se hace un xor que haces las veces de negar desde ai hasta bi 
	"""
	Mascara=1
	Mascara=(Mascara<<(bi-ai+1))# saca el numero de bits a ser cambiados mas uno (1000)
	Mascara=Mascara-1 #le resta uno con el fin de que queden todos en uno (111) pero entonces se le resta un bit por eso es la cantidad de los que quieren ser cambiados más uno
	Mascara=(Mascara<<(k-bi-1)) #completo con ceros la parte derecha restante 
	Nestado=Mascara^EI #realizo el xor entre la el decimal que representa el estado acutual con la mascara para tener como resultado la negación
	return (Nestado) 

def lights():
	
	EI=int(CI,16) #Estado inicial

	for i in range(0,M): #en este for recorro todos los estados dados por los m segundos
		
		ai,bi=lista[i]
		
		ZI=((EI>>(k-ai)) & 1) #realiza k-ai corrimientos a la derecha con el fin de que el ultimo bit del número decimal representado en binario sea el que esta en la posicion ai.Luego se hace un and con 1 para saber si lo que hay en esa posicion es un 1 o un 0 

		if  ZI == 0: # si en la posición ai hay un cero entonces busco el primer uno a la izquirda de ai-1(ai-1 porque inicia en cero)

			tmpAi=encontrarUnoAi(ai,EI) #Busco si hay un uno 
			if tmpAi==-1: # en caso de no encontrar un uno la función encontrarUnoAi devuelve -1
				ai=ai-1 # el extremo ai se cambia a ai-1 debido a que las posiciones empiezan en 0
			else:
				ai=tmpAi#en caso de encontrar el uno a la izquierda ai sera la posición donde se encontro el uno 
		else:
			ai=ai-1#si en la posición ai no hay un cero entonces solo le resto uno a ai porque empiezan en 0 las posiciones.

			
		ZD=(EI>>(k-bi) & 1)#realiza k-bi corrimientos a la derecha con el fin de que el ultimo bit del número decimal representado en binariosea el que esta en la posicion bi . Luego se hace un and con 1 para saber si lo que hay en la posición bi es un 0 o un 1 															

		if ZD == 0: #si en la posición bi hay un cero entonces busco el primer uno a la derecha de bi-1
			
			tmpBi=encontrarUnoBi(bi,EI)#Busco si hay un uno
			if tmpBi==-1:#en caso de no encotrar un uno la función encontrarUnoBi devuelve -1
				bi=bi-1 # el extremo bi se cambia a bi-1 debido a que las posiciones empieza en 0 pero los limites empiezan desde 1
			else:
				bi=tmpBi#en caso de encontrar el uno a la derecha bi sera la posición en la cual se encontro el uno 
		else:
			bi=bi-1	# si en la posición bi no hay un cero entonces solo le resto uno a bi porque empiezan en 0 las posiones.

		EI=negarCadena(ai,bi,EI) #se niega la cadena despues de establecer los limites según el enunciado del proyecto


	EF=hex(EI)[2:].upper()#pasar de decimal a hexadecimal (Estado final)
	print(EF)



def main():
	global k,M,lista,CI
	tcnt = int(stdin.readline())
	while tcnt!=0:
		k,M=map(int,stdin.readline().split()) # K es el número de bombillos y m el numero de segundos a considerar
		CI= stdin.readline()#Configuración inicial de las luces dada en hexadecimal.
		lista=[]
		for i in range(0,M):
			ai,bi=map(int,stdin.readline().split()) # K es el número de bombillos y m el numero de segundos a considerar
			lista.append((ai,bi))
		lights()
		tcnt=tcnt-1

main()
