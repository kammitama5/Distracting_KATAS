function evenOrOdd(str){
      var count1 = 0
      var count2 = 0
      for(var i=0;i<=str.length;i++){
          var a = (str[i])
          var b = parseInt(a)
          if (b % 2 == 0){
            count1 = count1 + 1
          }
          else{
            count2 = count2 + 1
          }
      }
      console.log(count1)
      console.log(count2)
      if (count1 > count2){
        console.log("Even is greater than Odd")
      }
      else if (count2 > count1){
        console.log("Odd is greater than Even")
      }
      else{
        console.log("Even and Odd are the same")
      }
  
  
  
}

evenOrOdd('12') //, 'Even is greater than Odd');
evenOrOdd('123')//, 'Odd is greater than Even');
evenOrOdd('112')//, 'Even and Odd are the same');

