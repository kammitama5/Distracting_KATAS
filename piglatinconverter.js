function pigLatin(phrase){
      arr = []
      a = phrase.toLowerCase()
      b = a.split(" ")
      for (var i = 0; i < b.length; i++){
        a = (b[i].slice(1)) + b[i].slice(0,1) + 'ay'
        arr.push(a)
        
      }
     w = arr.join(' ')
     return w
  
}
