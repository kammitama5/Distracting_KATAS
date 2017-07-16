var instancesOfN = function ( string, letter ) {
//insert your code here. 
  var total = 0;
  for (var i = 0; i < string.length; i++)
  {
    if (string[i] == letter){
      total = total + 1;
    }
  }
  if (total == 0)
  {
    return 'sorry no matches found'
  }
  else{
    return total;
  }

}

