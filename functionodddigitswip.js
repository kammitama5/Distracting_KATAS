function findOddDigits(n, k) {
    if (n < k){
      console.log(0)
      return 0;
    }
    else{
    var b = n.toString();
    var arr = []
    var arr1 = []
    var count = 0;
    //console.log(b)
    for (var i = 0; i < b.length; i++){
      arr.push(parseInt(b[i]))
    }
    //console.log(arr) 
    for (var i = 0; i < arr.length; i++)
    {
      if (arr[i] % 2 !== 0)
      {
        arr1.push(arr[i].toString());
        count = count + 1
        if (count == k){
          break;
        }
      }
      
    }
    arr2 = arr1.join("")
    console.log(arr2)
    return;
    }
}

