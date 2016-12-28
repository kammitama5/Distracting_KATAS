def length_of_line(array):
    w1, w2 = zip(*array)
    #print w1, w2
    side1  = (w2[1] - w2[0]) * (w2[1] - w2[0])
    side2 = (w1[1] - w1[0]) * (w1[1] - w1[0])
    hyp = (side1 + side2) ** 0.50
    
    return str("%.2f" % hyp)

