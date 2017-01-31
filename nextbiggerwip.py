from itertools import permutations
def next_bigger(n):
      arr = []
      #print n
      a = list(str(n))
      x = str(n)
      b = [''.join(c) for c in permutations(x)]
      #print b
      for i in b:
        if int(i) > n:
          arr.append(int(i))

      if len(arr) == 0:
        return -1 
      else:
        y = sorted(arr)
        return y[0]

      return
    
    
next_bigger(12)#21)
next_bigger(513)#531)
next_bigger(2017)#,2071)
next_bigger(414)#441)
next_bigger(144)#414)
next_bigger(9)#==-1
next_bigger(111)#==-1
next_bigger(531)#==-1