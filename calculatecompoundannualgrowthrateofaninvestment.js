function calculateCAGR(fv,pv,n){
      var inv = 1.0 / n
      var form = (((Math.pow((fv / pv), inv)) - 1) * 100.0)
      return eval(form.toFixed(2))
}
