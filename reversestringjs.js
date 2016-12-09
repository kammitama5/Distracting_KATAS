// easy reverse string in Javascript

function reverseString(str){
  var split = str.split("");
  var reverse1 = split.reverse();
  var join1 = reverse1.join("")
  return(join1)
}
