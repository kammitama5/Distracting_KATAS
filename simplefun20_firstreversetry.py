
def first_reverse_try(arr):

        arr1 = []
        if len(arr) < 2:
          a = arr 
          return arr
        else:
          a = arr[0]
          b = arr[-1]
          c = arr[1:-1]
          for i in c:
            d = i 
            arr1.append(d) 
          leng = len(arr1)
          arr1.insert(leng, a)
          arr1.insert(0, b)
          return arr1
            