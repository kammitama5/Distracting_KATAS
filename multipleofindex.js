function multipleOfIndex(array) {
  var arr = []
  for (var i = 0; i < array.length; i++)
  {
    if (array[i] % i == 0)
    {
      arr.push(array[i])
    }
  }
  return arr;
}

