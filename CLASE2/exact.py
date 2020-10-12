
#colaboradores: Miguel y Veronica T

from sys import stdin


def exact(valorP,cantM):

    INF = float('inf')
    ans=[]

    if (valorP,cantM) in diccionario:
        ans=diccionario.get((valorP,cantM))


    else:
        if valorP<=0 and cantM==0:
            ans=[0,0]

        elif valorP !=0  and cantM==0:
            ans=[INF,INF]
        else:
            temp=exact(valorP-denominaciones[cantM-1],cantM-1)
            nolatomo=exact(valorP,cantM-1)
            latomo=denominaciones[cantM-1]+temp[0],1+temp[1]

            if latomo[0]<nolatomo[0]:
                ans=latomo
            elif latomo[0]==nolatomo[0]:
                if latomo[1]<=nolatomo[1]:
                    ans=latomo
                else:
                    ans=nolatomo
            else:
                ans=nolatomo

        diccionario[valorP,cantM]=ans

    return ans


def main():
    global denominaciones,diccionario
    i=1
    tcnt = int(stdin.readline())

    while tcnt!=0:
        ans=None
        diccionario={}
        denominaciones=[]
        i=1
        valorP= int(stdin.readline())
        cantM = int(stdin.readline())
        while i <= cantM:
            denominaciones.append(int(stdin.readline()))
            i=i+1
        
        ans=exact(valorP,cantM) 
        print(ans[0],ans[1])
        tcnt -= 1


main()

