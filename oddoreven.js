function oddOrEven(array) {
    var total = 0;
   for (var i = 0; i < array.length; i++)
   {
     total = total + array[i]
   }
   if (array.length == 0){
     return "even"
   }
   else if (total % 2 == 0)
   {
     return "even"
   }
   else{
     return "odd"
   }
}

