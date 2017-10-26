def detect_operator(num):
    code = (str(num)[1:4])
    if (code == "039"):
      return "Golden Telecom"
    elif (code == "050") or (code == "066") or (code == "095"):
      return "MTS"
    elif (code == "063") or (code == "093"):
      return "Life:)"
    elif (code == "068"):
      return "Beeline"
    elif (code == "099"):
      return "MTS"
    elif (code == "067") or (code == "096") or (code == "097") or (code == "098"):
      return "Kyivstar"
    else:
      return "no info"
    return
	