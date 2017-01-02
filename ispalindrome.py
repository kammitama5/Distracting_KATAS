def is_palindrome(string):
    if type(string) == str:
        string1 = string.lower()
        if string1 == string[::-1]:
            return True
        else:
            return False
    if type(string) == int:
        str1 = str(string)
        if str1 == str1[::-1]:
            return True
        else:
            return False
			
			