function alternateSqSum(arr){
  count1 = 0
  count2 = 0
  count = 0
  for (var i = 0; i < arr.length; i++){
    if (arr.indexOf(i) % 2 == 0){
      a = (arr[i] * arr[i])
      count1 = count + a
      console.log(count1)
    }
    else{
      count2 = count + arr[i]
      //console.log(count2)
    }
  }
  console.log(count1)
  return count1 + count2
}

//alternateSqSum([])//,0)
//alternateSqSum([1,2,3,4,5])//,29)
alternateSqSum([-1,0,-3,0,-5,3])//,0)
//alternateSqSum([-1,2,-3,4,-5])//,11)
