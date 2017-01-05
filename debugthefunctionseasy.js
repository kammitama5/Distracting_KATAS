function multi(arr) {
  counter = 1
  for (var i = 0; i < arr.length; i++){
      counter = counter * arr[i]
  
  }
  return counter
}
function add(arr) {
  counter1 = 0
  for (var j = 0; j < arr.length; j++){
      counter1 = counter1 + arr[j]
  }
  return counter1 
}
function reverse(str) {
  a = str.split("").reverse().join("");
  return a
}
