function standardDeviation(values) {
          //console.log(values)
          arr = []
          sum = 0
          subt = 0
        
          
          for (var i = 0; i < values.length; i++){
            sq = values[i] * values[i]
            sum = sum + values[i]
            mean = ((sum) / values.length)

            arr.push(sq)
            subt = subt + ((values[i] - mean) ** 2.0)
          }
          
          
          //console.log(arr)
          //console.log(sum)
          //console.log(mean)
         
          //console.log(subt)
          meansqdiff = ((subt / values.length))
          //console.log(meansqdiff)
          sqroot = Math.sqrt(meansqdiff)
          return sqroot

}
