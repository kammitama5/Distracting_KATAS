function oddOne(arr) {
    var ans = -1
    for (var i = 0; i < arr.length; i++){
      if (arr[i] % 2 !== 0){
        ans = arr.indexOf(arr[i])
      }
      
    }
    return(ans)
}

