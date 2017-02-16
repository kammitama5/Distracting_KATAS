
function sumEvenNumbers(tbl_nombres) {
    var counter = 0 
    for (var i = 0; i <= tbl_nombres.length+1; i++){
      if (tbl_nombres[i] % 2 == 0){
        counter = counter + tbl_nombres[i]
      }
      }
    return counter
  
}
