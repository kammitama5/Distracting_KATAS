function checkVowel(string, position) {
  var allvowels = "aeiouAEIOU"
  var slicearr = allvowels.toLowerCase().split("")
  var str1 = string.toLowerCase().split("")
  for (var i = 0; i < slicearr.length; i++)
  {
    
    if (str1[position] == slicearr[i]){
      return true
    }
    else
    {
      return false
    }
  }

};
