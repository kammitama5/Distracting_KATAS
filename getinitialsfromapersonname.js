function toInitials(name) {
      arr = []
      var a = name.split(" ")
      for (var i = 0; i < a.length; i++){
        var g = (a[i][0]) + '.'
        arr.push(g)
      }
      var b = arr.join(" ")
      return b
}
