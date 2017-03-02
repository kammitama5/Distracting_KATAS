function alternateCase(s) {
  arr = []
  for (var i = 0; i < s.length; i++){
    if (s[i] == s[i].toUpperCase()){
      arr.push(s[i].toLowerCase())
    }
    else if (s[i] == s[i].toLowerCase()){
      arr.push(s[i].toUpperCase())
    }
    var b = arr.join("")
  }
  return b
  //return;
}
