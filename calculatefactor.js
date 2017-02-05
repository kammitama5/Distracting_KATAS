function factor(n){
   var arr = []
   for (var i = 1; i <= n; i++){
     if (n % i == 0){
       g = i
       arr.push(g)
     }
   }
    return (arr)
}
