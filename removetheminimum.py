def remove_smallest(numbers):
          arr = []
          if len(numbers) == 0:
            return []
          else:
            a = min(numbers)
            b = numbers.index(a)
            del numbers[b]
            return numbers
			