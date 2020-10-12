
from sys import stdin


def binaryStep(low,hi,x):

    ans=None

    if arr!=[]:

        while low<hi-1:

            mid=low+((hi-low)>>1)

            if arr[mid]>x:
                hi=mid

            elif arr[mid]<=x:
                low=mid

        if arr[low]<=x:
            ans=low

    return ans

def crearArr():

	global arr

	i=0
	c=0
	j=1
	arr=[1]#arreglo de diff

	while arr[-1] <= (2**31):
	
		if c==2:
			c=0
			j=j+1

		arr.append(arr[i]+j)


		i=i+1
		c=c+1

	return arr

def main():

	arr=crearArr()
	hi=len(arr)

	tcnt = int(stdin.readline())
	
	while tcnt!=0:
		tok = stdin.readline().split()
		A=int(tok[0])
		B=int(tok[1])
		diff=abs(B-A)
		pos=binaryStep(0,hi,diff)
		result=pos+1
		print(result)
		tcnt -= 1


main()

