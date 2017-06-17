function vowelFilter (letters) {
  var vowels = ["a", "e", "i", "o", "u"];
  var arr = [];
 for (var i = 0; i < letters.length; i++)
 {
   if ((letters[i] != "i") && (letters[i] != "a") && (letters[i] != "e") && (letters[i] != "o") && (letters[i] != "u"))
   {
     arr.push(letters[i])
   }
  
 }
 
  return arr;
};

