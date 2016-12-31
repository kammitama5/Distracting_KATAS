def high_and_low(numbers):
    h = numbers.split()
    w = map(int, h)
    sort1 = sorted(w)
    sort2 = map(str, sort1)
    
    
    ans = sort2[-1] + " " + sort2[0]
    ans1 = ''.join(ans)
    print ans1
	
	