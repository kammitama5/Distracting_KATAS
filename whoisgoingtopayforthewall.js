function whoIsPaying(name){
  var arr = [];
  if (name.length <= 2){
    arr.push(name)
    return arr;
  }
  else{
    var trunc = name.substring(0,2);
    arr.push(name)
    arr.push(trunc)
    return arr;
  }
}

