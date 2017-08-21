function percentageSumArray(arr){
        if ((arr == null) || (arr.length) == 0){
          return false
        }
        else{
          var total = 0
          var total1 = 0
          var num = 0
          for (var i = 0; i < arr.length; i++){
            total = total + arr[i]
            if (arr[i] > 0){
              num = num + 1
              total1 = total1 + arr[i]
            }
          }
          var percent = ((num / 100) * total)
          if (percent == 0){
            return false
          }
          else if ((percent < 0) && (total < 0)){
            return false
          }
          else if (isNaN(percent) == true){
            return false
          }
          else{
          var percent2 = ((num / 100 ) * total1)
          var percent1 =  Math.round(percent * 100) / 100
          return percent1
          }
        }
        return
}
