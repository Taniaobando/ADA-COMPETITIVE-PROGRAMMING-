#Nombre: Tania C. Obando S.
#Codigo: 6036110

from sys import stdin

def transp(x,ans):

  global mxans
  
  if x==NT:
    mxans.append(ans)

  else:

    (s,t,p)=ordenes[x]

    estacion=s
    while estacion<=t:
      train[estacion]+=p
      estacion+=1
    train[t]-=p

    if train[s]<=CP:
      transp(x+1,ans+((t-s)*p))
    estacion=s
    while estacion<=t:
      train[estacion]-=p
      estacion+=1
    train[t]+=p
    transp(x+1,ans)


def main():

  global ordenes,NT,train,mxans,CP

  linea= stdin.readline().strip().split()

  while linea!=['0','0','0']:
      ordenes=[]
      CP=int(linea[0]) #Capacidad de pasajeros
      DF=int(linea[1]) #Numero de estacion de destino(B)
      NT=int(linea[2]) #Numero de triplas que hay con la estacion de partida, la estacion de detino y el numero de pasajeros 
      ordenes=[]
      for i in range(0,NT):
        
        tok = stdin.readline().strip().split()
        EP=int(tok[0]) #estacion de partida
        ED=int(tok[1]) #estacion de destino
        NP=int(tok[2]) #numero de pasajeros
        ordenes.append((EP,ED,NP))
      
      mxans=list()
      DF+=1
      train=[0]*DF
      ordenes.sort(key=lambda x:x[0])
      transp(0,0)
      ans=max(mxans)
      print(ans)
      linea= stdin.readline().strip().split()


main()