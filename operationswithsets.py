def process_2arrays(arr1, arr2):
    a = sorted(arr1)
    b = sorted(arr2)
    arr = []
    One = list(set(a) & set(b))
    Two = len(list(set(a) | set(b))) - len(One)
    Three = len(list(set(a))) - len(One)
    Four = len(list(set(b))) - len(One)
    Zero =  len(One)
    arr.append(Zero)
    arr.append(Two)
    arr.append(Three)
    arr.append(Four)
    
    return arr
	
	