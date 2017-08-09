function stringTask(s){
  arr = []
  s = s.replace(/a|e|i|o|y|A|O|E|I|Y|U|u/gi, '');
  for (var i = 0; i < s.length; i++)
  if ((s[i] != 'a') || (s[i] != 'e') || (s[i] != 'i') ||
  (s[i] != 'o') || (s[i] != 'u') || (s[i] != 'A') ||
  (s[i] != 'E') || (s[i] != 'O') || (s[i] != 'U') || (s[i] != 'y') || (s[i] != 'Y')){
    arr.push('.'+s[i].toLowerCase())
  }
  var a = arr.join('')
  //console.log(a)
  return a
}
