from sys import stdin

diccionario= {65:[],66:[],67:[],68:[],69:[],70:[],71:[],72:[],73:[],74:[],75:[],76:[],77:[],78:[],79:[],80:[],81:[],82:[],83:[],84:[],85:[],86:[],87:[],88:[],89:[],90:[],97:[],98:[],99:[],100:[],101:[],102:[],103:[],104:[],105:[],106:[],107:[],108:[],109:[],110:[],111:[],112:[],113:[],114:[],115:[],116:[],117:[],118:[],119:[],120:[],121:[],122:[]}


def solve(cadena, subcadena):

    contador3=0
    temp=-1
    listemp=[]
    aux=1
    while contador3 < len(subcadena):
        key=ord(subcadena[contador3])
        arr=diccionario[key]
        temp=binarySearchM(arr,0,len(arr),temp)
        listemp.append(temp)

        contador3=contador3+1

        if temp == -1:
            aux=0
            contador3=len(subcadena)


    if aux==0:
        print("Not matched")
    else:
        print("Matched",listemp[0],listemp[len(listemp)-1])




def llenarDiccionario(cadena):

    if cadena != "":
        contador=0

        for caracter in cadena:
            key=ord(caracter)
            diccionario[key].append(contador)
            contador=contador+1

        return(diccionario)

def binarySearchM(arr,low,hi,x):
    ans=-1

    if arr!=[]:        

        while low+1<hi:
    
            mid=low+((hi-low)>>1)

            if arr[mid]>x:
                hi=mid
                ans=arr[mid]
            else:
                low=mid
    

        if (arr[low]>x):
            ans=arr[low]
    
    return(ans)


def main():
    cadena = stdin.readline().strip()
    tcnt = int(stdin.readline())
    diccionario=llenarDiccionario(cadena)
    while tcnt != 0:
        subcadena = stdin.readline().strip()
        solve(cadena, subcadena)
        tcnt -= 1
main()

