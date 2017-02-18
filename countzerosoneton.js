function countZeros(n) {
        var count = 0;
        for (var i = 1; i <=n; i++){
          a = i.toString()
          for (var j = 0; j < a.length; j++)
          if (a[j] == '0'){
            count = count + 1
          }
          else if (a[j] == '00'){
            count = count + 2
          }
          else if (a[j] == '000'){
            count = count + 3
          }
        }
        //console.log(count)
        return count
}
