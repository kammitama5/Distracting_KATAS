
def calculate_payment(p0, amortization, interestRate):
        r = interestRate / (12.0 * 100.0)
        N = amortization * 12.0 
        a = (1.0 + r) ** (-N)
        
        
        c = (r * p0) / ((1 - ((1 + r)**(-1 * N))))
        return round(c, 2)
		