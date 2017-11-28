// given an array of ints, return the sum
// of all the ints that have an even index,
// multiplied by the int at the last index.
// array empty, return 0

function evenLast(numbers) {
  if (numbers.length === 0)
  {
    return 0;
  }
  else{
  var count = 0;
  var lastindex = numbers[numbers.length-1]
  
  for (var i = 0; i < numbers.length; i++)
  {
    if (([i] % 2 === 0))
    {
      count = count + numbers[i]
    }
  }
  var finalcount = count * lastindex;
  return finalcount;
  }
}