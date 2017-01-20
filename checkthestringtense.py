def check_tense(word):

    if word[-2:] == "ed":
        return "Past"
    else:
        return "Present"
		
		