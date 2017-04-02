function add (x, y) {
	while(y)x^=y,y=(y&x^y)<<1
  return x;
}

