function isAlt(word) {
 console.log(word)
 var odds = []
 var evens = []
 
 for (var i = 0; i < word.length; i++)
  if ((word[0] == 'a') || (word[0] == 'e') || (word[0] == 'i') ||
  (word[0] == 'o') || (word[0] == 'u')){
    if (i % 2 == 0){
      evens.push(word[i]);
    }
    else{
      odds.push(word[i])
    }
  }
  console.log(evens)
  return
}

isAlt("amazon")
// true
isAlt("apple")
// false
isAlt("banana")
// true
