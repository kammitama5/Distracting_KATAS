def getSlope(p1, p2):
    if (p2[1] == p1[1]):
        return 0
    elif (p2[1] - p1[1] == 0):
        return None
    elif ((p1[0] == p2[0]) and (p1[1] == p2[1])):
        return None
    else:
        y = (p2[1] - p1[1])
        x = (p2[0] - p1[0])
        ans = y / x
        if ans == 0:
            return None
        else:
            return ans
			
			