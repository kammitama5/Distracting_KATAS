function isPartOfFibonacciSequence(input){
  var one = 0;
  var two = 1;
  while (one <= input){
    if (one == input){
      return true;
    }
    two = one + two;
    one = two - one;
  }
  return false;
}

