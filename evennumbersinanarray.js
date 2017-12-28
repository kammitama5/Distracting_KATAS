function evenNumbers(array, number) {
  // good luck
  var arr = []
  for (var i = 0; i < array.length; i++)
  {
    if (array[i] % 2 === 0)
    {
      arr.push(array[i])
    }
  }
  return arr.slice(-number) 
}

