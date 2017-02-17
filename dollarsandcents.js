function formatMoney(amount){
  a = '$' + amount.toFixed(2).replace(/(\d)(?=(\d{3})+\.)/g, '$1');
  return a
}
