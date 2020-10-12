import math
from sys import stdin

#Colaboradores: Laura Arango, Veronica Tofiño, Xavier Garzon,Danilo Melgarejo


def flight(a,m):

    ans=0
    INF=float("inf")
    A=a
    M=m
    
    tab=[[INF for _ in range(M+1)] for _ in range(10)]
    tab[9][0]=0
    m=1
    a=9

    while m != M+1:
        if a<0:
            a=9
            m=m+1
        else:
            if a>0 and a<9:
                
                tab[a][m]=min(tab[a-1][m-1]+60-matrizW[a-1][m-1],
                    tab[a+1][m-1]+20-matrizW[a+1][m-1],tab[a][m-1]+30-matrizW[a][m-1])         
            
            elif a==0:
                
                tab[a][m]=min(tab[a+1][m-1]+20-matrizW[a+1][m-1], tab[a][m-1]+30-matrizW[a][m-1])
                
            elif a==9: 
                tab[a][m]=min(tab[a-1][m-1]+60-matrizW[a-1][m-1], tab[a][m-1]+30-matrizW[a][m-1])

            a=a-1
            
    return(tab[9][M])


def main():

    global matrizW
    tcnt= int(stdin.readline())
    while tcnt!=0:
        espacio=stdin.readline()
        millas=int(stdin.readline())//100
        matrizW=[]
        altura=9
        i=1
        while i <= 10:
            temp=list(map(int,stdin.readline().split()))
            matrizW.append(temp)
            i=i+1
        result=flight(altura,millas)
        print(result)
        print("")
        tcnt=tcnt-1

main()


