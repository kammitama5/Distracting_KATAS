def round_to_2_decimal_places(n):
    from decimal import Decimal
    return float(round(Decimal(n), 2))
	
	