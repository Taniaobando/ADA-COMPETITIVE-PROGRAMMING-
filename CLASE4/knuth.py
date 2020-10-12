#Nombre: Tania C. Obando S.
#Codigo= 6036110
#Colaboradores: Codigo hablado con cardona.

from sys import stdin

def knuth(idx,ans):
	if idx==len(tcnt):
		print("".join(ans))

	else:
		copia=list(ans)
		for k in range(0,idx+1):
			ans.insert(k,tcnt[idx])
			knuth(idx+1,ans)
			ans=list(copia)


def main():
	global tcnt
	tcnt= stdin.readline().strip()
	while tcnt != "":
		ans=knuth(0,list())
		print("")
		tcnt=stdin.readline().strip()

main()

