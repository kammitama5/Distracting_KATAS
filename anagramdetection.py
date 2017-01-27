def is_anagram(test, original):
        a = test.lower()
        a1 = sorted(a)
        x = ('').join(a1)

        b = original.lower()
        b1 = sorted(b)
        y = ('').join(b1)

        
        if x == y:
          return True
        else:
          return False
        return
		