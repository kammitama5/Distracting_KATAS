function fibsFizzBuzz(n) {
  var a = 1, b = 0, total = 0, arr = [], arr1 = [], temp;

  while (n > 0){
    temp = a;
    a = a + b;
    b = temp;
    arr.push(b)
    n--;
    
  }
  for (var i = 0; i < arr.length; i++){
    if ((arr[i] % 3 == 0) && (arr[i] % 5 == 0)){
      arr1.push("FizzBuzz")
    }
    else if (arr[i] % 3 == 0){
      arr1.push("Fizz")
    }
    else if (arr[i] % 5 == 0){
      arr1.push("Buzz")
    }
    else{
      arr1.push(arr[i])
    }
  }
  
  
  return arr1;
}
