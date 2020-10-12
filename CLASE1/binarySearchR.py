def binarySearch(low,hi,x):
    arr=[1,2,3,4]

    ans=-1
    if  low+1==hi:
        if arr[low]==x:
            ans=low

    else:
        mid=low+((hi-low)>>1)

        if arr[mid]>x:
            ans=binarySearch(low,mid,x)
        elif arr[mid]<x:
            ans=binarySearch(mid,hi,x)
        
        else:
            ans=mid
    print(ans)
    
    return ans

def main():
    binarySearch(0,4,3)

main()