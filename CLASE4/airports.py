#Nombre: Tania C. Obando S.
#Codigo: 6036110

from sys import stdin

class dforest(object):
  """Disjoint-Union implementation with disjoint forests using path
  compression and ranking"""

  def __init__(self, size=100):
    """create an empty disjoint forest"""
    self.__parent = [ i for i in range(size)]
    self.__rank = [ 0 for _ in range(size)]
    self.Naeropuertos=0


  def __str__(self):
    """return the string representation"""
    return str(self.__parent)
  
  def find(self, x):
    """return the representative of x"""
    if self.__parent[x]!=x: self.__parent[x] = self.find(self.__parent[x])
    return self.__parent[x]

  def union(self, x, y):
    """perform the union of the collections where x and y belong"""
    rx,ry = self.find(x),self.find(y)
    if rx!=ry:
      krx,kry = self.__rank[rx],self.__rank[ry]
      if krx>=kry:
        self.__parent[ry] = rx
        if krx==kry: self.__rank[rx] += 1
      else:
        self.__parent[rx] = ry


def kruskal(G, lenv):

  ans = list()
  G.sort(key=lambda x: x[2])
  df = dforest(lenv)
  acum=0
  kha=0
  df.Naeropuertos=lenv

  for u,v,w in G:
    u=u-1
    v=v-1
   
    if df.find(u)!=df.find(v):
      if ca > w: 
        ans.append((u, v, w))
        df.union(u, v)
        df.Naeropuertos-=1
        acum=acum+w

  kha=df.Naeropuertos*ca+acum
  return kha,df.Naeropuertos


def main():
  global ca
  tcnt= int(stdin.readline())
  cnt=1
  while tcnt!=0:
    ans=None
    Grafo=[]
    nc,ncll,ca = map(int,stdin.readline().split()) 
    i=1
    while i <= ncll:
      temp=list(map(int,stdin.readline().split()))
      Grafo.append(temp)
      i=i+1
  
    ans,Naeropuertos=kruskal(Grafo,nc)
    print("Case #{0}: {1} {2}".format(cnt,ans,Naeropuertos))
    tcnt=tcnt-1
    cnt=cnt+1



main()