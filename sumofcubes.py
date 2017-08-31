def sum_cubes(n):
    cube = 0
    
    for i in range(1, n+1):
      cube = cube + (i * i * i)

    return cube