def merge_arrays(arr1, arr2):

        for i in arr2:
          arr1.append(i)
        
        
        b =  sorted(arr1)
        c = list(set(b))
        print sorted(c)

        return
		