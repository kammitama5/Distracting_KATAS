function parse( data )
{     count = 0
      arr = []
      //console.log(data)
      a = data.split('')
      for (var i = 0; i < a.length; i++){
        if (a[i] == 'i'){
          count = count + 1
        }
        else if (a[i] == 'd'){
          count = count - 1
        }
        else if (a[i] == 's'){
          count = count * count
        }
        else if (a[i] == 'o'){
          arr.push(count)
        }
        
      }
      return (arr)
}
