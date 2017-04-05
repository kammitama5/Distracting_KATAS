function ConvertMeIntoANumber(array) {
 var arr = []
 for (var i = 0;i < array.length; i++)
 {
   if (parseInt(array[i]) == array[i]){
     arr.push((eval(array[i])))
   }
   else{
     arr.push(NaN)
   }
 }  
    return(arr)
}
