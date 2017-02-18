def count_red_beads(N_blue):
    if N_blue <= 1:
        return 0
    else:
        total = (N_blue - 1) * 3.0
        red = (2.0 / 3.0) * total
        return red
		