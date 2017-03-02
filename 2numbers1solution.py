def get_op(num1, num2, target):
    
    if (num1 + num2) == target:
      return "add"
    elif (num1 - num2) == target:
      return "subtract"
    elif (num1 * num2) == target:
      return "multiply"
    elif (num1 / num2) == target:
      return "divide"
	  
	  