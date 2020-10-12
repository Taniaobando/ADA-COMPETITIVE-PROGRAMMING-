from sys import stdin

def backpack(res):
    sumi=0
    cnt=0
    i=0
    while i<=nc:
        if(arr[i]>res):
            return 0;
        if(sumi+arr[i]>res):
            sumi=arr[i]
            cnt=cnt+1
        else:
            sumi=sumi+arr[i]
        i+=1

    if sumi:
        cnt=cnt+1
    return cnt <=nk


def bin():

    l=0
    r=1000000
    mid=0
    while l<=r:
        mid=(l+r)>>1
        if(backpack(mid)):
            r=mid-1
        else:
            l=mid+1

    return (r+1)

def main():
    global arr,nc,nk

    linea=stdin.readline()


    while linea!='':
        nc,nk = map(int,linea.split())
        arr=[]
        nk+=1
        i=1
        ans=None
        mid=0
        while i <= nc+1:
            arr.append(int(stdin.readline()))
            i=i+1
    
        ans=bin()
        print(ans)

        linea = stdin.readline()


main()