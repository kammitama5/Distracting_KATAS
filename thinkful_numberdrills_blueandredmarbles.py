def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    totalleft = (blue_start - blue_pulled) + (red_start - red_pulled)
    blue = (blue_start - blue_pulled)
    return (((blue * 10.0) / (totalleft * 10.0)) / 1.0)
	