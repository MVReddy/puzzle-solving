import sys
import re

# cat .\input.txt | python sudoku.py
def read_in():
  lines = sys.stdin.readlines()
  for i in range(len(lines)):
    lines[i] = lines[i].replace('\n','')
  return lines

def stringMatch(today, last):
  if re.search(''.join(today).replace('0','\d'), ''.join(last)):
    return True
  else:
    return False

def swapindexes(today, last, i=3):
  for value in range(0, 10, 3):
    if value < i or i > length:
      continue
    a = last[:]

    for _ in range(2):
      a.insert(i, a[i-2])
      a.pop(i-2)
      
      if stringMatch(today, a) or\
         swapindexes(today, a, i+3):
        return True

      for __ in range(2):
        a.insert(i, a[i-3])
        a.pop(i-3)

        if stringMatch(today, a) or\
           swapindexes(today, a, i+3):
          return True

  return False

def swapSets(a, i, j, f):
  a = a[:] + a[f(i, j)]
  for _ in range(i):
    a.pop((i-j)*i)
  return a

def compareSet(today, last):
  f = lambda i,j: slice((i-j)*i, (i-j)*i+3)

  a = last[:]
  for _ in range(2):
    a = swapSets(a, 3, 2, f)
    if stringMatch(today, a):
      return True

    for __ in range(2):
      a = swapSets(a, 3, 3, f)
      if stringMatch(today, a):
        return True

  return False

length = 9
#rows = ["963174258", "178325649", "254689731", "821437596", "496852317", "735961824", "589713462", "317246985", "642598173", "060104050", "200000001", "008305600", "800407006", "006000300", "700901004", "500000002", "040508070", "007206900"]
#print rows

inp = read_in()
for v in range(1, len(inp), len(inp) / int(inp[0])):
  rows = inp[(v):(v)+length*2]
  rowslast = rows[:length]
  rowstoday = rows[length:length*2]
  rowslast_reversed = rowslast[:]
  rowslast_reversed.reverse();

  columnstoday = ['']*length
  columnslast = ['']*length
  for i, _ in enumerate(rowstoday):
    for j, __ in enumerate(rowstoday):
      columnstoday[i] += rowstoday[j][i]
      columnslast[i] += rowslast[j][i]

  columnslast_reversed = columnslast[:]
  columnslast_reversed.reverse()
         
  if stringMatch(rowstoday, rowslast) or\
     stringMatch(columnstoday, columnslast_reversed) or\
     stringMatch(rowstoday, rowslast_reversed) or\
     stringMatch(columnstoday, columnslast) or\
     swapindexes(rowstoday, rowslast) or\
     swapindexes(columnstoday, columnslast) or\
     compareSet(rowstoday, rowslast) or\
     compareSet(columnstoday, columnslast):
    print 'Yes'
  else:
    print 'No'