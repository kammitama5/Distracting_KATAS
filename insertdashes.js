function insertDash(num) {
   var arr = []
   var a = num.toString()
   for (var i = 0; i < a.length; i++){
     if ((a[i] % 2 !== 0) && (a[i+1] % 2 !== 0))
      arr.push(a[i]+'-')
     else{
       arr.push(a[i])
     }
   }
   var b = arr.join('')
   if (b[b.length-1] == '-')
    return(b.slice(0,b.length-1))
   else{
     return(b)
   }
}
