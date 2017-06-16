function scf(array){
    var arr = []
    var a = Math.min.apply(null, array)
    //console.log(a)
    for (var i = 2; i <= a; i++)
    {
      for (var j = 2; j < array.length; j++ )
      {
        if (array[j] % i === 0){
          arr.push(i)
        }
      }
    }
    console.log(arr[2])
    return
}
