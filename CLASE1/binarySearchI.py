def binary(low,hi,x):

    arr=[0,1,2,7]

    ans=None

    if arr!=[]:

        while low+1<hi:

            mid=low+((hi-low)>>1)

            if arr[mid]>x:
                hi=mid

            elif arr[mid]<x:
                low=mid
            else:
                ans=mid
                hi=low+1
    print(ans)
    return ans


def main():
    binary(0,4,2)

main()