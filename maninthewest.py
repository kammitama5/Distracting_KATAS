def check_the_bucket(bucket):
    total = 0
    for i in bucket:
        if i == 'gold':
            total = total + 1
    if total == 0:
        return False
    else:
        return True
		