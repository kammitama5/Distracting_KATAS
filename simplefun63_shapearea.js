function shapeArea(n) {
      var total = 1
      for (var i = 1; i <= n; i++){
        var r = 4 * (i - 1)
        total = total + r
      }
      return total
}
