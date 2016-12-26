def duty_free(price, discount, holiday_cost):
  wanton = holiday_cost / (price * (discount / 100.0))
  print int(wanton)