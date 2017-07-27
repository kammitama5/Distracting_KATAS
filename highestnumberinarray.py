def highestNum(nums):
    try:
        s = sorted(nums)
        return s[-1]
    except:
        return 0
    