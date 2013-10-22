import sys
import re

# cat .\input.txt | python phonelist.py
def read_in():
  lines = sys.stdin.readlines()
  for i in range(len(lines)):
    lines[i] = lines[i].replace('\n','')
  return lines

def phonelist(a):   
  for i, _ in enumerate(a):
    if i is len(a)-1: break
    for j, __ in enumerate(a):
      if j is 0: continue 

      if i is not j:
        if(re.search("^" + a[i], a[j])):
          return 'No'
  return 'Yes'

inp = read_in()
k = 1
for v in range(int(inp[0])):
  a = inp[(k+1):int(inp[k])+(k+1)]
  k+= int(inp[k])+1
  a = sorted(a, cmp=lambda a,b: int(a) - int(b))
  print phonelist(a)