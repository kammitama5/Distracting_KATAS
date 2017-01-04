function replaceVogals(str){
      arr = []
      for (var i = 0; i < str.length; i++){
          if ((str[i] == "a") || (str[i] == "i") || (str[i] == "o") ||
          (str[i] == "e") || (str[i] == "u") || (str[i] == "A") ||
          (str[i] == "E")
          || (str[i] == "O") || (str[i] == "U") || (str[i] == "I")){
            
              arr.push("?")
          }
          else{
              arr.push(str[i])
          }
      }
      y = arr.join("")
      return(y)
  
}

