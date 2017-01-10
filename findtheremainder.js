function remainder(a, b){
   if ((a == 0) || (b == 0)){
     console.log("NaN")
     }
   else if (b < a){
     console.log((a % b))
   }
   else{
     console.log((b % a))
   }
  
}
