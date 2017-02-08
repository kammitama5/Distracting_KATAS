function trailingZeros(num, base){
        product = 1 
        for (var i = 1; i <= num; i++){
          product = product * i
        }
        console.log(product)
        var a = (product).toString(base)
        
        var b = (a.match(/0/g) || []).length
        console.log(b)
        
        
        
        
        
        return
}
