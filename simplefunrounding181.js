function rounding(n, m) {
  var mult = n % m; // remainder
  var div = parseInt(n / m); // division
  //console.log(div)
  var mid = (m / 2.0);
  //console.log(mid)
  if ((n < m) && ((n / (m * 1.0)) < 0.5)){
    //console.log(0)
    return 0;
  }
  else if (mult < mid){
    //console.log(div * m)
    return(div * m);
  }
  else if (mult > mid){
    //console.log(((div + 1) * m))
    return(((div + 1) * m))
  }
  else{
    //console.log(n)
    return(n);
  }

}
