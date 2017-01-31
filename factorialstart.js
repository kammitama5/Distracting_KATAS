function factorial(n){
        product = 1
        for (var i = 1; i < n+1; i++){
          product = product * i
        }
        a = (Number(product).toPrecision())
        b = (n).toString() + '!'
        return a
}
