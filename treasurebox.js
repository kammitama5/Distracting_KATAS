function findNum(n){
  result = 0
  n = n.toLowerCase()
  var a = n.replace(/[^\w\s!.]/g,'');
  var b = a.replace(/ /g,'')
  for (var i = 0; i < b.length; i++){
    if (b.indexOf('one') !== -1){
      result = 1
    }
    else if (b.indexOf('two') !== -1){
      result = 2 
    }
    else if (b.indexOf('three') !== -1){
      result = 3
    }
    else if (b.indexOf('four') !== -1){
      result = 4
    }
    else if (b.indexOf('five') !== -1){
      result = 5
    }
    else if (b.indexOf('six') !== -1){
      result = 6
    }
    else if (b.indexOf('seven') !== -1){
      result = 7
    }
    else if (b.indexOf('eight') !== -1){
      result = 8
    }
    else if (b.indexOf('nine') !== -1){
      result = 9
    }
    else if (b.indexOf('ten') !== -1){
      result = 10
    }
  }
  return result
}
