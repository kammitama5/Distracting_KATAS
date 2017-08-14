function flipper(stringArr){
    return stringArr.reverse().map(function(item) {
    if (item.length == 1){
      return item
    }
    else
   
    return item.slice(0, item.length-1).toLowerCase()+ item.charAt(item.length-1).toUpperCase() 
  }).join(" ");
  
}
