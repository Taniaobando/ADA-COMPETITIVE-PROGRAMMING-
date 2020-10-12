#Nombre: Tania C. Obando S.
#Codigo: 6036110

from sys import stdin

def solve(L, G, lista):
	lista.sort(key=lambda x:x[0],reverse=False)

	ans,low,n,N, ok = list(),0,0,len(lista),True 
	while ok and low < L and n != G:
		ok = lista[n][0] <= low
		best,n = n,n+1
		while ok and n != N and lista[n][0] <= low:
			if lista[n][1] > lista[best][1]:
				best = n
			n += 1
		ans.append(best)
		low = lista[best][1]
	ok = ok and low >= L
	if not ok:
		ans = []
	return len(ans)


def main():
	linea = stdin.readline().strip().split()
	
	while linea != ['0','0']:
		lista = []
		LC = int(linea[0]) #longitud del camino 
		NG = int(linea[1]) #Número de estaciones en servicio
		for i in range(NG):
			tok = stdin.readline().strip().split()
			centro = int(tok[0])
			radio = int(tok[1])
			lista.append([centro-radio,centro+radio])
		ans = solve(LC,NG,lista)
		if ans == 0:   
			print(-1)
		else: 
			print(NG-ans)
		linea = stdin.readline().strip().split()

main()
