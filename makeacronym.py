def to_acronym(input):
        arr = []
        a = input.split(" ")
        for i in a:
          x = i[0].upper()
          arr.append(x)
        y = ('').join(arr)
        return y
		