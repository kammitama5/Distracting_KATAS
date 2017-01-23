def triple_trouble(one, two, three):
        x = ""

        for a, b, c in zip(one, two, three):
          a =  [a + b + c]
          for i in a:
            x += i
        print x
		