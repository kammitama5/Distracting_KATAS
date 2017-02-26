function whichOne(arr) {
    var arr1 = [];
    for (var i = 0; i < arr.length; i++){
      if (arr[i] == "Just Right"){
        arr1.push("Code-ilocks")
      }
      else{
        arr1.push(arr[i])
      }
    }
    return arr1
}
