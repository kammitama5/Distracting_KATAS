from itertools import permutations
def next_bigger(n):
      arr = []
      a = str(n)
      b = list(a)
      c = permutations(b)
      for i in list(c):
        d = i
        e = ''.join(d)
        f = arr.append(int(e))
      g = sorted(arr)
      #print g
      for i in g:
        w = g.index(n)
      if g[w+1] == n:
        return g[w+2]
      else:
        return g[w+1]
      
        
      

      
        
      return



next_bigger(12) #21)
next_bigger(513) # 531)
next_bigger(2017) #2071)
next_bigger(414) #441)
next_bigger(144) #414)