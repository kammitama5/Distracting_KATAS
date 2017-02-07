def camel_case(string):
      arr = []
      a = string.strip()
      b = a.split(" ")
      for i in b:
        arr.append(i.title())
      arr1 = ''.join(arr)
      return arr1
	  