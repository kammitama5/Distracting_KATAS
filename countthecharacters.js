function countChar(string, char){
  count = 0
  s = string.toLowerCase()
  c = char.toLowerCase()
  for (var i = 0; i < s.length; i++)
  {
    if (string[i].toLowerCase() == c){
      count = count + 1
    }
  }
  console.log(count)
  
}



countChar("fizzbuzz", "z") // should return 4 
countChar("Fancy fifth fly aloof", "f") // should return 5