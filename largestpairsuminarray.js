function largestPairSum(numbers)
{
      d =numbers.sort((a,b)=>a-b);
      e = d.slice(1).slice(-2)
      total = 0
      for (var i = 0; i < e.length; i++){
        total = total + e[i]
      }
      
      return total

}

