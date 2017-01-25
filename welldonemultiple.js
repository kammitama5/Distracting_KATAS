
function multiplus(array){
     var arr = []
     for (var i = 0; i < array.length; i++){
       if ((array[i] % 2 == 0) && (array[i] % 3 == 0)){
         a = "Well Done"
         arr.push(a)
       }
       else if (array[i] % 2 == 0){
         a = "Well"
         arr.push(a)
       }
       else if (array[i] % 3 == 0){
         a = "Done"
         arr.push(a)
       }
       
     }
     return arr
}
