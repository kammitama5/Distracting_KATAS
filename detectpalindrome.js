function isPalindrome(str){
  if (str.split("").reverse().join("").toLowerCase() == str.toLowerCase()){
    return true
  }
  else{
    return str
  }
}
