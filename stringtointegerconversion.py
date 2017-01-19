def my_parse_int(string):
    try: 
        int(string)
        return int(string)
    except ValueError:
        return "NaN"
		
		