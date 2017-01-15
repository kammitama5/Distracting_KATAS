def rot_energies(B, Jmin, Jmax):
        arr = []
        if (Jmin > Jmax) or (B < 0):
          return []
        else:
          for i in range(Jmin, (Jmax + 1)):
            c = (B *i) *(i+1)
            arr.append(c)
          return arr
		  
		  