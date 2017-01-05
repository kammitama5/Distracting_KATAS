var palindromeChecker = function(string) {
  a = string.toLowerCase()
  b = a.split("").reverse().join("")
    if (a == b){
      return true
    }
    else{
      return false
    }
  