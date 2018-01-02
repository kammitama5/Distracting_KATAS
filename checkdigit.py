def check_digit(number, index1, index2, digit):
    a = (list(str(number)))
    arr = []
    arr.append(index1)
    arr.append(index2)
    arr = sorted(arr)
    bool = False
    for i in range(arr[0], arr[1]+1):
      if str(a[i]) == str(digit):
        bool = True
        break;
      else:
        bool = False
    return bool
	