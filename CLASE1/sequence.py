from sys import stdin

def dig_up_to(n):

	if n<10:
		ans=n
	elif n<100:
		ans=9+((n-9)*2)
	elif n<1000:
		ans=189+((n-99)*3)
	elif n<10000:
		ans=2889+((n-999)*4)
	elif n<100000:
		ans=38889+((n-9999)*5)
	else:
		ans=0
	return ans

def sequence(pos):
	#print(arr)
	pos=pos-1
	#print("pos:",pos)

	temp=binarySearchM(arr,0,len(arr),pos)
	#print("temp:",temp)
	result=pos-temp
	#print("result :",result)
	numb= sec[result]

	print(numb)
	


def binarySearchM(arr,low,hi,x):
    
    if arr!=[]:

        while low<hi-1:

            mid=low+((hi-low)>>1)

            if arr[mid]>x:
                hi=mid

            elif arr[mid]<=x:
                low=mid

        if arr[low]<=x:
            ans=arr[low]

    return ans



def arregloDlow(n):

    contador=1
    lista=[0]
    
    while  contador <n:
        temp= dig_up_to(contador)
        lista.append(temp+lista[contador-1])
        contador=contador+1
    return(lista)


	
def generarSecuencia(n):      
	"""
	lista=''.join(str(i) for i in range(1,n))	
	"""

	lista=""

	contador=1
	while  contador <= n:
		lista+=(str(contador))
		contador=contador+1

	return (lista)



def main():

	tcnt = int(stdin.readline())
	n=31278
	global sec,arr
	sec=generarSecuencia(n)
	arr=arregloDlow(n)
	while tcnt!=0:
		pos=int(stdin.readline())
		sequence(pos)
		tcnt -= 1



"""
def main():
   	
   	n=31278
	global sec,arr

   	sec=generarSecuencia(n)
	arr=arregloDlow(n)
	pos=271458232
	sequence(pos)
"""
main()
