palindrome = function(str) {
        str1 = str.toLowerCase()
        str2 = str1.split('').reverse().join('');
        if (str2 == str1){
          return true
        }
        else
          return false
}
