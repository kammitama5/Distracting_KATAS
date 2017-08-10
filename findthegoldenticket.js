function finder(box) {
 var box1 = box.reduce(function(a, b) {
  return a.concat(b);
});
  var d = box1.indexOf(true)
  if (d == -1){
    return "There is no golden ticket!"
  }
  else{
  return d
  }
}
