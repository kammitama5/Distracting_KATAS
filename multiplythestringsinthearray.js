function arrMultiply(arr){
   var total = 1
   for (var i = 0; i < arr.length; i++){
     if (arr[i] == '0'){
     total = 0
     }
     else
     {
      total = total * parseInt(arr[i])
   }
   }
   return(total.toString())
}

