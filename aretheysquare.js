var isSquare = function(arr){
        arr1 = []
        if ((arr.length) == 0){
          return (undefined)
        } 
        else{
          // if square -> true
          for (var i = 0; i < arr.length; i++){
            if (Math.sqrt(arr[i]) % 1 === 0) {
              arr1.push("True")
            }
            else{
              arr1.push("False")
          }
          
          }
          for (var j = 0; j < arr1.length; j++){
            if (arr1[j] == "False"){
              g = false
            }
            else{
              g = true
            }
          }
          return (g)
        }
}
