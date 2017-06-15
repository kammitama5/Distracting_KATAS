function mostFrequent(arr, limit)
{
  
  var arr1 = Array.from(new Set(arr));
  var arr2 = []
  
  for (var i = 0; i < limit; i++)
  {
    arr2.push(arr1[i])
  }
  return (arr2)
}

mostFrequent(['x','g','x','t','g','x'], 2)//,['x','g'])
mostFrequent(['c','b','b','a','a','a'], 3)//,['a','b','c'])
mostFrequent(['k','j'], 1)//,['k'])

