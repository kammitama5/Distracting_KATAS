function surviveFirst(str){
    if (str.length <= 1){
      return (str)
    }
    else{
      var a = str.length - 1
      return (str[0] + '*'.repeat(a)) 
    }
}
