function stringBreakers(n, string){
    var arr = []
    string = string.replace(/\s+/g, '');
    for (var i = 0; i < string.length+1; i++){
      if (i % n == 0){
        arr.push(string[i-1] + '\n')
      }
      else
        arr.push(string[i-1])    
    }
    var b  = arr.join("")
    b = b.replace(/\s*$/,"");
    return(b.slice(10,b.length))
}

