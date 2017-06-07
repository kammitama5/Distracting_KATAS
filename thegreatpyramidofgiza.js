function buildPyramidTime(strength, skill) {
  // Only change code below this line
  var total = strength + skill;
  
  if (total > 15)
  {
    return "receive 3000 gold coins"
  }
  else if ((total >= 10) && (total <= 15)){
    return "receive 5000 gold coins"
  }
  else
  {
    return "receive 10000 gold coins"
  }
    // Only change code above this line
  }
  
  