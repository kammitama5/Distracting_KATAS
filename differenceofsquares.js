
function differenceOfSquares(x){

        count = 0
        count1 = 0
        for(var i = 0; i < x+1; i++){
          a = Math.pow(i, 2)
          b = i
          count1 = count1 + b
          count = count + a
         
        }
        var x = (count)
        var y = (count1 * count1)
        var diff = y - x
        return (diff)
}
