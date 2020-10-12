from sys import stdin

def comp(sumi, ans, k):
  aux = 0
  aux = sumi - k
  while(aux % 2 != 0):
    ans += 1
    aux += ans
  return ans

def solve(K):
  ans, k = 0, abs(K)
  low, hi = 0, 1000000000
  ok = False
  if k == 0: k = 2
  while (low <= hi) and not ok:
    mid = low + ((hi - low) >> 1)
    sumi = (mid * (mid + 1)) >> 1 #Formula sumatoria n*(n+1)/2
    if(k == sumi):
      ans = mid
      ok = True
    elif (k < sumi):
      if (k > (mid * (mid - 1)) >> 1): # Para no tomar el ultimo valor de la sumatoria
        ans = mid
        ans = comp(sumi, ans, k)
        ok = True
      hi = mid
    else: 
      low = mid #La sumatoria es menor que el k, se mueve el limite de low
  return ans
 
def main():
  tcnt,first = int(stdin.readline()),True
  while tcnt != 0:
    stdin.readline()
    if first == False: print()
    first = False
    print(solve(int(stdin.readline())))
    tcnt -= 1

main()