  function skiponacci(n) {
        var i;
        var fib = []
        arr = [] 
        arr1 = ['1']
        fib[0]  = 0;
        fib[1] = 1;
        
        for (var i = 2; i <= n; i++){
          fib[i] = fib[i-2] + fib[i-1]
          
          arr.push(fib[i])
          
        }
        for (var i = 0; i < arr.length; i++){
          if (i % 2 != 0){
            arr1.push(arr[i] + " skip")
          }
        }
        b = arr1.join(' ')
        //console.log(b)
        if (b.length == 1){
          return("1")
        }
        else{
          return("1 skip " + b.slice(2, -5))
        }
}
