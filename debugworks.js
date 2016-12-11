function multi(arr) {
  
  var prod = 1
  for (var i = 0; i < arr.length; i++){
    prod *=arr[i]
  }
  
  return(prod)
  
}
function add(arr) {
  total = 0
 for (var i = 0; i < arr.length; i++){
    total += arr[i]
  }
  
  return(total)
}
  
function reverse(str) {
  var spl = str.split("")
  var potato1 = spl.reverse();
  var potato2 = spl.join("")
  //console.log(potato1)
  return(potato2)
  }
  




//multi([5, 1, 5]) // returns 25
//multi([2, 3, 5]) // returns 30
add([9, 8, 5]) // 22
add([1, 2, 3]) // returns 6
//reverse("hello")

