def house_numbers_sum(inp):
    count = 0
    for i in inp:
        count = count + i
        if i == 0:
            break;
    return count
	