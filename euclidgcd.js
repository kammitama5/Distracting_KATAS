function euclidGcd(a,b){
  if (!b) {
    return a;
  }
  return euclidGcd(b, a % b);

}

