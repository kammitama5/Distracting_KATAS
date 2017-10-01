function capitalize(s){
   var first = ""
   var second = ""
   arr = []
   for (var i = 0; i < s.length; i++){
     if (i % 2 == 0){
       first += s[i].toUpperCase()
       second += s[i].toLowerCase()
     }
     else{
       first += s[i].toLowerCase()
       second += s[i].toUpperCase()
     }
   }
   arr.push(first)
   arr.push(second)
   return(arr)
};

