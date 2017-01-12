def tax(x):
    if type(x) == str:
        return "Error 404"
    else:
        a = x + (.05 * x)
        return a
		