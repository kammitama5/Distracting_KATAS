# different version of Euler problem -> found on CodeWars
# just modified my Euler algo
def solution(number):
  number = range(0, number)
  theSum = 0
  for i in number:
      if (i % 3 == 0) or (i % 5 == 0) :
          theSum = theSum + i
  return theSum
