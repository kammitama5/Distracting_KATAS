var say = function(string1) {
  return function(say){
    return string1 + ' ' + say;
  }
}
