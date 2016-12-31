import math 

def quadratic_formula(a, b, c):
    ans = []
  
    root1 = (((-1 * b) + (math.sqrt((b * b) - (4 * a * c)))) /( 2 * a))
    root2 = (((-1 * b) - (math.sqrt((b * b) - (4 * a * c)))) /( 2 * a))

    ans.append(root1) 
    ans.append(root2)
    return ans