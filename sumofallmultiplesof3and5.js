function findSum(n) {
      counter = 0
      for (var i = 0; i < n+1; i++){
          if (i % 3 == 0){
              counter = counter + i
          }
          else if (i % 5 == 0) {
              counter = counter + i
          }
          else{
              counter = counter
          }
      
      }
     return counter 
}

