function filterEvenLengthWords(words) {
  var arr = []
  for (var i = 0; i < words.length; i++)
  {
    if (words[i].length % 2 === 0){
      arr.push(words[i])
    }
  }
  //console.log(arr)
  return arr
}
