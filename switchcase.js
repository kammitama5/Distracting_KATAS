function switchCase (str) {
  var str1 = [];
  for (var i = 0; i < str.length; i++)
  {
    if (str[i].toLowerCase() == str[i]){
      str1.push(str[i].toUpperCase())
    } 
    else
  {
        (str1.push(str[i].toLowerCase()))
  }
  }
  var str2 = str1.join("");
  return str2
}

