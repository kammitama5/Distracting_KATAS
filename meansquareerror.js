var solution = function(firstArray, secondArray) {
              arr = []
              count = 0
              for (var i = 0; i < firstArray.length; i++){
                  var a = secondArray[i] - firstArray[i]
                  var b = (a * a * 10.0) / 10.0
                  arr.push(b)
                 
                }
              var c = firstArray.length
              for (var j = 0; j < arr.length; j++){
                count = count + arr[j]
              }
              return (count / c)
              
}

