def small_enough(array, limit):

    if all(i <= limit for i in array):
        return True
    else:
        return False
		