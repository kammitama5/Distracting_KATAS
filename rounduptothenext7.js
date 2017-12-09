function roundUpNext7(number) {
  if (number % 7 === 0){
    return number;
  }
  else if ((number % 7 <= 3) && (number > 0))
  {
    var num = (parseInt(number / 7) + 1) * 7
    return num
  }
  else if ((number % 7 <= 4) && (number <= 0))
  {
    var num = (parseInt(number / 7.0)) * 7.0 
    return num
  }
   else if (((number % 7 >= 4)) && (number > 0)){
    var num = number / 7 
    var modd = number % 7 
    return(((parseInt(num)) + 1) * 7)
  }
  
}

