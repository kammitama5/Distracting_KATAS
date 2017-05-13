def validate_code(code):
    code1 = str(code)
    
    if code1.startswith("1"):
      return True
    elif code1.startswith("2"):
      return True
    elif code1.startswith("3"):
      return True
    elif len(code1) > 3:
      return False
    else:
      return False
	  