function onesComplement(n) {
    var arr = []
    for (var i = 0; i < n.length; i++){
      if (n[i] == '1'){
        arr.push('0')
      }
      else if (n[i] == '0'){
        arr.push('1')
      }
    }
    g = arr.join('')
    
    return g
};
