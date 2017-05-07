 function isPalindrome(stringToTest) {
    if (typeof(stringToTest) != 'string'){
      return false
    }
    else{
    var stringToTest1 = stringToTest.toString().replace(/[^0-9a-z]/gi, '')
    return (stringToTest1.toLowerCase() == stringToTest1.split('').reverse().join('').toLowerCase());
   }
}

