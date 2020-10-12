from sys import stdin
from math import sqrt


def grass(l,w,lista):
  lista.sort(key=lambda x:x[0]) #De menor a mayor por la primera componente de la tupla
  ans=[]
  low=0
  n=0
  N=len(lista)
  ok=True
  
  while ok and low<l and n!=N:
    ok=lista[n][0]<=low
    best=n
    n=n+1
    while ok and n!=N and lista[n][0]<=low:
      if lista[n][1]>lista[best][1]:
        best=n
      n+=1
    ans.append(best)
    low=lista[best][1]
  ok = ok and low>=l
  if ok==False:
    ans = []
  return(len(ans))

def dx(R, W):
  return (sqrt((R*R) - ((W*W)/4)))

def main():

  linea=stdin.readline()
  while linea != "":
    lista=[]
    N,l,w=map(int,linea.split())
    tcnt=N
    while tcnt!=0:

      c,r= map(int,stdin.readline().split())
      if r > w/2:
        lista.append((c-dx(r,w),c+dx(r,w)))
      tcnt-=1
  
    ans = grass(l,w,lista)
    if ans == 0: print(-1)
    else: print(ans)
    linea=stdin.readline()

main()
