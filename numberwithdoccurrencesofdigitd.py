def is_dd(n):
    a = list(str(n))
    answer = []
    for i in a:
      if a.count(i) == int(i):
        answer.append("True")
        
    if len(answer) > 0:
      return True
    else:
      return False