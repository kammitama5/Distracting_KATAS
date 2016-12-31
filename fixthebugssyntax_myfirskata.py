def my_first_kata(a,b):
    if type(a) != int or type(b) != int:
        return False
    return a%b+b%a
	
	