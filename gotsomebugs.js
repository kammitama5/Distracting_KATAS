function logicalCalc(array, op){
      //console.log(array)
      var found = false;
      //AND
      function alltrue(one){
        return one == true;
      }
      if (op == "AND"){
        if (array.every(alltrue)){
          found = true
        }
      }
      //OR
      if (op == "OR"){
        for(var i = 0; i < array.length; i++){
          if (array[i] === true){
            found = true;
          }
        }
      }
      //XOR
      if (op == "XOR"){
        for (var i = 0; i < array.length; i++){
          if ((array[i] === true) && (!array.every(alltrue))){
            found = true;
          }
          else if ((array.length == 1) && (array[i] == true)){
            found = true;
          }
        }
      }
      return found
}
