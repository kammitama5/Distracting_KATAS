function passed (list) { 
    total = 0 
    count = 0
    for (var i = 0; i < list.length; i++){
      if (list[i] <= 18){
        total = total + list[i] 
        count = count + 1
      }
    }
    if (isNaN(total / count)){
      return('No pass scores registered.')
    }
    else{
      return(Math.round(total * 1.0 / count * 1.0))
    }
} 
