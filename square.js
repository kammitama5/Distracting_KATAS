function squareRoot(numbers){
  
   var total = 0;
   for (var i = 0; i < numbers.length; i++){
     total = total + numbers[i]
   }
   
   var a = Math.sqrt(total)
   if (total == 0){
     return(0)
   }
   else if (a == parseInt(a)){
     return(a)
   }
   else{
     return(total)
   }
}
