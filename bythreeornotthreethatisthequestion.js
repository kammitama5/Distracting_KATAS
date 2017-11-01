function divisibleByThree(str){
    var sum = 0;
    for (var i = 0; i < str.length; i++){
      sum = sum + parseInt(str[i])
    }
    if (sum % 3 === 0){
      return true
    }
    else{
      return false
    }
}
