from sys import stdin
import math


#La formula fue tomada del siguiente link https://www.algorithmist.com/index.php/UVa_846

def solve(a,b):
	ans=0
	dist=b-a

	temp=(math.sqrt(4*dist))-1
	ans=int(math.ceil(temp))

	print(ans)		




def main():
  tcnt = int(stdin.readline())
  while tcnt!=0:
    tok = stdin.readline().split()
    solve(int(tok[0]), int(tok[1]))
    tcnt -= 1

main()

