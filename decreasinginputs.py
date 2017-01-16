def add(*args):
    count = 0
    for index, a in enumerate(args):
      g = (a / (index + 1.0))
      count = count + g
    return int(round(count, 0))
