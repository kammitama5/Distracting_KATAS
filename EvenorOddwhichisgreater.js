function evenOrOdd(str){
        
        var a = str.split('')
        count = 0
        count1 = 0
        for (var i = 0; i < a.length; i++){
          b = parseInt(a[i])
          if (b % 2 == 0){
            count = count + b
          }
          else{
            count1 = count1 + b
          }
       
          
        }
        if (count > count1) {
          return("Even is greater than Odd")
        }
        else if (count < count1){
          return("Odd is greater than Even")
        }
        else{
          return("Even and Odd are the same")
        }
        
        
  
  
}

