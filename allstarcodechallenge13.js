function translate(word){
        word1 = word.toLowerCase()
        if (word.length < 2){
          return word
        }
        
        else if ((word1[0] == 'a') || (word1[0] == 'e')
        || (word1[0] == 'i') || (word1[0] == 'o')
        || (word1[0] == 'u')){
          return (word + "ay")
          
        }
        else{
          
          return (word.slice(1) + word.slice(0,1) + 'ay')
        }
       
}
