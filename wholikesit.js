function likes(names) {
  var a = names.length
  
  if (a == 0){
    return 'no one likes this'
  }
  else if (a == 1){
    return names[0]  + ' likes this'
  }
  else if (a == 2){
    return names[0] + ' and ' + names[1] + ' like this'
  }
  else if (a == 3){
    return names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this'
  }
  else if (a > 3){
    return names[0] + ', ' + names[1] + ' and ' + (a - 2).toString() + ' others like this'
  }
}
