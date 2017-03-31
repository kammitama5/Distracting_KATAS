function palindrome(num) { 
  if (typeof(num) != 'number' || (num < 0)){
    return("Not valid")
  }
  else{
    var num1 = num.toString()
    var num2 = num1.split('').reverse().join('')
    if (num1 == num2){
      return(true)
    }
    else{
      return(false)
    }
  }
} 
