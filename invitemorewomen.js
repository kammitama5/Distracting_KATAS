function inviteMoreWomen(L) {
  var count = 0 
  var count1 = 0
  arr1 = []
  for (var i = 0; i < L.length; i++){
    b = L[i].toString()
    arr1.push(b)
  }

  for (i = 0; i < arr1.length; i++){
    if (arr1[i] == 1){
      count = count + 1
    }
    else if (arr1[i] == -1){
      count1 = count1 + 1
    }
  }
  
  if (count > count1){
    return(true)
  }
  else{
    return(false)
  }
  
}
