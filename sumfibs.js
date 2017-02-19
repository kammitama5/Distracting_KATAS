function sumFibs(n) {
  var a = 1, b = 0, total = 0, arr = [], temp;

  while (n >= 0){
    temp = a;
    a = a + b;
    b = temp;
    arr.push(b)
    n--;
    
  }
  for (var i = 0; i < arr.length-1; i++){
    if (arr[i] % 2 === 0){
      total = total + arr[i];

    }
  }
  
  return total;
}
