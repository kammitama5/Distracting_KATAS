function printValues(n){
  for (var i = 1; i < 101; i++){
    if (i % 7 === 0){
      return "Code"
    }
    else if ((i % 5 === 0) && (i % 3 != 0)){
      return "Wars"
    }
    else{
      return i
    }
    
  }
}

