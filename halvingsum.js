function halvingSum(n)
{ 
  sum = 0
  var i = n;
  while (parseInt(i) != 1)
  {
    sum = sum + parseInt(i)
    i = i / 2
  }
  
  return(sum + 1)
  
  
}

