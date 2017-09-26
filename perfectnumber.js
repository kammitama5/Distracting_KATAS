function isPerfect(number){
  var sum = 0
  for (var i = 1; i < number; i++){
    if (number % i == 0)
    {
      sum = sum + i 
      
    }
  }
  
  if (sum == number)
  {
    
    return(true)
  }
  else
  {
    return(false)
  }
}