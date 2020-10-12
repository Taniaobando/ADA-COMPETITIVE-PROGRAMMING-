from sys import stdin,setrecursionlimit
setrecursionlimit(11000)

INF = float('inf')

def cut(startWood, endWood):
    ans=INF
    if(startWood+1==endWood):
        return 0
    else:
        if(startWood,endWood) in diccionario:
            ans=diccionario.get((startWood,endWood))
            

        else:
            for i in range(startWood+1,endWood):
                ans= min(ans,cut(startWood,i) + cut(i,endWood)+(A[endWood]-A[startWood]))
            diccionario[(startWood,endWood)]=ans
    return ans

def main():
    
    global A, diccionario

    l = int(stdin.readline())
    while(l != 0):
        diccionario={}
        A=[]
        n = int(stdin.readline())
        A = list(map(int,stdin.readline().split()))
        A.insert(0,0)
        A.insert(n+1,l)      
        print("The minimun cutting is {0}.".format(cut(0,n+1)))
        l = int(stdin.readline())    

main()