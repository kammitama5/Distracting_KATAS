def how_many_times(annual_price, individual_price):
      div = annual_price / individual_price
      if  (annual_price % individual_price == 0):
        return div
      else:
        return int(div) + 1
		
		