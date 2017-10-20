function arrayLowerCase(arr) {
    var arr1 = []
    for (var i = 0; i < arr.length; i++)
    {
      if ((typeof(arr[i]) === 'string')){
        arr1.push(arr[i].toLowerCase())
      }
      else{
        arr1.push(arr[i])
      }
    }
    return arr1
}

