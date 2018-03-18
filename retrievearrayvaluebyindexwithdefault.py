def solution(items, index, default_value):
    try:
        if (len(items) -1)  < (index):
            return items[default_value]
        else:
            return items[index]
    except:
        return default_value