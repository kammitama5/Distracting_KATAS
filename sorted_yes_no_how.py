def is_sorted_and_how(arr):
    a = sorted(arr)
    b = a[::-1]
    if arr == a:
      return "yes, ascending"
    elif arr == b:
      return "yes, descending"
    else:
      return "no"
      