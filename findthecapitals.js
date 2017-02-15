function capitals(word){
    arr = []
    for (var i = 0; i < word.length; i++){
      if (word[i] == word[i].toUpperCase()){
        g = word.indexOf(word[i])
        arr.push(g)
      }
    }
    return (arr)

}

