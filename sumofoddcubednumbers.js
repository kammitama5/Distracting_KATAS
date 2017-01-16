function cubeOdd(arr) {
      if (!arr.some(isNaN)){
        count = 0
        for (var i = 0; i < arr.length; i++)
        {
            g = (arr[i] * arr[i] * arr[i])
            if (g % 2 != 0){
              w = g 

              count = count + w
            }
            
          
      }
        }
      else{
        return undefined
      }
      return count


}

