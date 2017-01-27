def zebulansNightmare(functionName):
            a = functionName
            b = a.split('_')
            arr = []
            for i in b:
              if len(b) > 1:
                c = i[0].upper() + i[1:]
                arr.append(c)
              else:
                c = i
                arr.append(c)
            d = ('').join(arr)
            return d[0].lower() + d[1:]
			