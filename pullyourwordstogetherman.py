def sentencify(words):
    words = " ".join(words)
    return words[0].upper() + words[1::] + "."
	