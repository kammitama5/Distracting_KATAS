 function scrabbleScore(str){
        str = str.toLowerCase()
        var count = 0;
        for (var i = 0; i < str.length; i++){
          if ((str[i] == 'a') || (str[i] == 'e') || (str[i] == 'i') || (str[i] == 'o') || (str[i] == 'u') || (str[i] == 'l') || (str[i] == 'n') || (str[i] == 'r') || (str[i] == 's') || (str[i] == 't')){
            
            count = count + 1
          }
          else if ((str[i] == 'd') || (str[i] == 'g')){
            count = count + 2
          }
          else if ((str[i] == 'b') ||  (str[i] == 'c') ||
          (str[i] == 'm') || (str[i] == 'p')){
            count = count + 3
          }
          else if ((str[i] == 'f') ||(str[i] == 'h') ||
          (str[i] == 'v') || (str[i] == 'w') || (str[i] == 'y')){
            count = count + 4
          }
          else if (str[i] == 'k'){
            count = count + 5
          }
          else if ((str[i] == 'j') || (str[i] == 'x')){
            count = count + 8
          }
          else if ((str[i] == 'q') || (str[i] == 'z')){
            count = count + 10
          }
 
        }
        return count 
        //return count
} 