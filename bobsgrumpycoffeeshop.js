function getCoffee(ar, cof) {
  var sum = 0.0
  for (var i = 0; i < ar.length; i++)
  {
    sum = sum + ar[i]
  }
  
  if ((sum == 2.20 && cof == "Americano") || (sum == 2.30 && cof == "Latte") || (sum == 2.40 && cof == "Flat white") || (sum == 3.50 && cof == "Filter")){
    return "Here is your Latte, have a nice day!"
  }
  else
  {
    return "Sorry, exact change only, try again tomorrow!"
  }
}

