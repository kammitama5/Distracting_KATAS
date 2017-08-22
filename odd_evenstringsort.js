function sortMyString(S) {
    
    var arr = []
    var arr1 = []
    for (var i = 0; i < S.length; i++){
      if (i % 2 == 0){
        arr.push(S[i])
      }
      else{
        arr1.push(S[i])
      }
    }
    var a = arr.join("")
    var b = arr1.join("")
    var d = (a + " " + b)
    return d
}
