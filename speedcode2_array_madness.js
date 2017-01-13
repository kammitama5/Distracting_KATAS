function arrayMadness(a, b){
        var count = 0
        var count1 = 0
        for (var i = 0; i < a.length; i++){
          count = count + (a[i] * a[i])
        }

        for (var j = 0;  j < b.length; j++){
          count1 = count1 + (b[j] * b[j] * b[j])
        }
        
        
        if (count > count1){
          return true
        }
        else{
          return false
        }
        
      
}



arrayMadness([4, 5, 6], [1, 2, 3])

