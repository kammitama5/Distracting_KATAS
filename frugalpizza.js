function pizzaPrice(diameter, price) {
  var area = Math.PI * ((diameter / 2.0) *(diameter / 2.0))
  var ppi = price * 1.0 / area * 1.0
  if (ppi == 0){
    return 0
  }
  else if ((price == undefined) || (diameter == undefined)){
    return 0
  }
  else if (price == null){
    return 0;
  }
  else if ((isNaN(price) === true) || (isNaN(ppi))){
    return 0;
  }
  else if (price === NaN)
  {
    return 0;
  }
  else{
    return eval(ppi.toFixed(2));
  }
  
}
