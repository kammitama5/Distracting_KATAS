"""
there is a 6 digit
number starting 100 
and is divisible by 9127
"""

total = 0
for i in range(100000,100999):
  if i % 9127 == 0:
    total = i
print total

# answer 100397