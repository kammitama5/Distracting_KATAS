function capitalize(s,arr){
  var arr1 = []
  var a = "";
  for (var i = 0; i < s.length; i++){
    for (var j = 0; j < arr.length; j++){
      if (i == arr[j]){
        arr1.push(s[i].toUpperCase())
        break;
      }
      
    }
   if (i !== arr[j])
   arr1.push(s[i].toLowerCase())
   
  }
  var b = arr1.join("")
  //console.log(b)
  return b
};
