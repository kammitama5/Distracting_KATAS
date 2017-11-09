  function sumOfDiff(n) {
    var sum = 0;
    var sum1 = 0;
    for (var i = 0; i <= n; i++)
    {
      sum = sum + (i * i)
      sum1 = sum1 + i
    }
    var total = (sum1 * sum1) - sum
    var string1 = total.toString()
    var string2 = string1.split("")
    var arr = [];
    var finalsum = 0;
    for (var j = 0; j <= string2.length-1; j++)
    {
      var square =  parseInt(string2[j]) * parseInt(string2[j])
      finalsum = finalsum + square
    }
    return finalsum
}
