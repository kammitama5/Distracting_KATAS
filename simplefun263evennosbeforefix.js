function evenNumbersBeforeFixed(sequence, fixedElement) {
      var total = 0;
      var arr = []
      if (!(sequence.includes(fixedElement) === true)){
        return(-1)
      }
      
      
        var a = sequence.indexOf(fixedElement)
        //console.log(a)
        for (var i = 0; i < a; i++){
          if (sequence[i] % 2 === 0)
          {
            total = total + 1;
            //arr.push(total)
          }
        }
      
      return total
}
