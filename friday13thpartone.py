def kill_count(counselors, jason):
    arr = []
    for i in counselors:
      if i[1] < jason:
        arr.append(i[0])
    return arr
	