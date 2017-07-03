function check(a,x){
  if(RegExp('\\b'+x+'\\b').test(a.join(','))){
    return true
    }
  else{
    return false
  }
}
