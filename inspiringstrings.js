function longestWord(stringOfWords){
    var arr = [];
    var arr1 = [];
    var a = stringOfWords.split(" ");
    
    for (var i = 0; i < a.length; i++)
      {
        arr.push(a[i].length)
      }
    
    var max = Math.max.apply(null, arr)
    
    for (var i = 0; i < arr.length; i++)
    {
      if (a[i].length == max){
        arr1.push(a[i])
      }
    }
    
    return(arr1[arr1.length-1])
  
}

