def better_than_average(class_points, your_points):
    counter = 0
    length = len(class_points)
    for i in class_points:
        counter = counter + i
        average = counter / length
    
    if your_points > average:
        return True
    else:
        return False
        
        
better_than_average([1,2,3,4], 5)
better_than_average([10, 9, 8, 10], 3)

