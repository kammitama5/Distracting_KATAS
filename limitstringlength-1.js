function solution(string,limit){
    if (limit < string.length){
      return (string.slice(0, limit) + "...") 
    }
    else{
      return string
    }
}
