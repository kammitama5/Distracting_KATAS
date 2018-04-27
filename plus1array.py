def up_array(arr):
    h = ""
    if len(arr) == 0:
        return None
    for i in arr:
        if ((i < 0) or (i > 9)):
            return None
        else:
            h = h + str(i)
    g = int(h) + 1
    j = str(g)
    w = list(j)
    arr = []
    for i in w:
      arr.append(int(i))
    return arr 