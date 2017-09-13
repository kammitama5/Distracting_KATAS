function isNormal(n){
 // tis so cute `^(~_~)^`
 var arr = []
 if (n < 1){
   return false
 }
 else{
   for (var i = 2; i < n; i++){
     if ((n % i === 0) && (i % 2 !== 0)){
       arr.push(i)
     }
   }
   if (arr.length === 0){
     return(true)
   }
   else{
     return(false)
   }
   return
  }
}

