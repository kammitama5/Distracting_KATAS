def buy_or_pass(stock_price, all_time_high):
    if (stock_price <= (.80 * all_time_high)):
        return "Buy"
    else:
        return "Pass"
		
		