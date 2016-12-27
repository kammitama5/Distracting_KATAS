def parse_float(string):
        str1 = ''.join(string)
        if str1.replace('.','',1).isdigit():
            return float(str1)
        else:
            return None
			
			