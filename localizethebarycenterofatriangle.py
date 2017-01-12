def bar_triang(pointA, pointB, pointC):

      arr = []
      
      xa = pointA[0]
      xb = pointB[0]
      xc = pointC[0]
      
      ya = pointA[1]
      yb = pointB[1]
      yc = pointC[1]
      
      barya = (xa + xb + xc) / 3.00 
      baryb = (ya + yb + yc) / 3.00

      
      bary1 = round(barya, 4)
      bary2 = round(baryb, 4)
      
      arr.append(bary1)
      arr.append(bary2)
      
      return arr
  