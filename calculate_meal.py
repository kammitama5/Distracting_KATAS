def calculate_total(subtotal, tax, tip):
    a = (float(subtotal) + ( (float((tax + tip)) / 100.00) * subtotal))
    return round(a, 2)
    
   
  
  





calculate_total(5.00, 5, 10) # 5.75
calculate_total(36.97, 7, 15)# 45.10
calculate_total(0.00, 6, 18) # 0.00
calculate_total(80.94, 0, 20) # 97.13
calculate_total(54.96, 8, 0) # 59.36


