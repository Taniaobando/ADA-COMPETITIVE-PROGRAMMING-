#Colaboradores: Veroonica Tofiño
#Elaborado por: Tania C. Obando S.


from sys import stdin

def moliu(k):

    cont=0
    
    if k==0:
        cont=0

    else:
        while k>3:
            #print(k,"k2")
            if k%2==0:
                k=k//2
                cont+=1
                #print("no")

            else:
            
                if ((k-1)//2)%2==0:
                    #print("het")
                    k-=1
                    cont+=1

                elif ((k+1)//2)%2==0:
                    #print("kha")
                    k+=1
                    cont+=1
      
    if k==1:
        cont+=1
    if k==2:
        cont+=2
    if k==3:
        cont+=3
    
    print(cont)


def main():
    k=0
    linea=stdin.readline()
    while linea != "":
        k=int(linea)
        moliu(k)
        linea=stdin.readline()

main()








"""
def main():
    k=0
    linea=stdin.readline()
    while linea != "":
        k=int(linea)
        moliu(k)
        linea=stdin.readline()

main()
"""