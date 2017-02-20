function iccanobif(n) {
  var a = 1, b = 0, total = 0, arr = [], arr1 = [], temp;

  while (n > 0){
    temp = a;
    a = a + b;
    b = temp;
    arr.push(b)
    n--;
  }
    return arr.reverse()
  }
  