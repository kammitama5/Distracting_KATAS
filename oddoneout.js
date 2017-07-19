function oddNum(arr) {
  var arr1 = []
  for (var i = 0; i < arr.length; i++)
  {
    if (arr[i] % 2 != 0)
    {
      arr1.push(i)
    }
  }
  if (arr1.length == 0){
    return -1;
  }
  else{
  return arr1[0]
  }
}

