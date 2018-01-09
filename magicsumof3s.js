function magicSum(numbers) {
  var arr = []
  var count = 0;
  var check = "3";
  if ((numbers == null) || (numbers.length == 0)){
    return 0;
  }
  else
  {
    for (var i = 0; i < numbers.length; i++)
    {
      arr.push(numbers[i].toString())
    }
    for (var j = 0; j < arr.length; j++)
    {
      if (arr[j].includes(check) && (arr[j] % 2 !== 0)){
        count = count + parseInt(arr[j])
      }
    }
  }
  return count;
}
