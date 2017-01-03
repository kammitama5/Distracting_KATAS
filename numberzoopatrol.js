sum up elements in array
sum up range if all total there
subract total from sum in array

function findNumber(array) {
  var sum = array.reduce(add, 0);

  function add(a, b) {
    return a + b;
    
}

  // sum => console.log(sum)
  
  
  y = array.length + 1
  counter = 0
  for (var i = 0; i < y + 1; i++){
      counter = counter + i;
  }
  //console.log(counter)
  answer = counter - sum
  console.log(answer)
  return
  
}

