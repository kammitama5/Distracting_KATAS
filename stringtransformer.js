function stringTransformer(str) {
      arr = []
      a = str.split(" ").reverse()
      b = a.join(" ")
      for (var i = 0; i < b.length; i++){
        if (b[i] == b[i].toUpperCase()){
          arr.push((b[i]).toLowerCase())
        }
        else{
            arr.push(b[i].toUpperCase())
        }
      }
      w = arr.join("")
      return w
}

