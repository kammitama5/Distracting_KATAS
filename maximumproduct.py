def adjacent_element_product(array):
    temp = array[0] * array[1]
    for i in range(0, len(array)-1):
      x = array[i]
      y = array[i+1]
      if (x * y) > temp:
          temp = x * y;
    return temp;