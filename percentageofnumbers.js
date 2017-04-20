function percentageSumArray(arr){
        //console.log(arr)
        var total = 0;
        var arr1 = []
        if (arr == null){
          return(false);
        }
        else{
          for (var i = 0; i < arr.length; i++){
            if (arr[i] >= 1){
              arr1.push(arr[i])
            }
          }
          //console.log(arr1)
          for (var i = 0; i < arr1.length; i++){
            total = total + arr1[i]
          }
          var perc= arr1.length / 100.0 
          return(total * perc)
        }
        
        //return
}
 