function vowelIndices(word){
  var arr = []
  var word1 = word.toLowerCase()
  for (var i = 0; i < word1.length; i++){
    if (word1[i] == 'a'){
      arr.push(i+1)
    }
    else if (word1[i] == 'e'){
      arr.push(i+1)
    }
    else if (word1[i] == 'i'){
      arr.push(i+1)
    }
    else if (word1[i] == 'o'){
      arr.push(i+1)
    }
    else if (word1[i] == 'y'){
      arr.push(i+1)
    }
    else if (word1[i] == 'u'){
      arr.push(i+1)
    }
  }
  return(arr)
}
