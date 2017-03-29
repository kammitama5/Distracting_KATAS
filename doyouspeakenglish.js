function spEng(sentence){
    var a = sentence.toLowerCase()
    var sub = "english";
    if (a.includes(sub)){
      return(true)
    }
    else{
      return(false)
    }
}

