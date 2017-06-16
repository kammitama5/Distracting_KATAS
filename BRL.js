function currencyBRL(number) {
  if (number == null){
    var a = 'R$ 0,00'
  }
  else{
    var a = ('R$ ' + number.toFixed(2).replace(/(\d)(?=(\d{3})+\.)/g, '$1,'));
    var a = a.replace(".", ",");
  }
  return a
}
