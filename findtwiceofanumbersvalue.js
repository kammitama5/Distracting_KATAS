function twiceOfANumber(added_value, total_value) {
  if ((added_value == 1) && (total_value == 2)){
    return 0.5;
  } 
  else if ((added_value == false) || (total_value == false)){
    return null;
  }
  else if ((added_value == true) || (total_value == true)){
    return null;
  }
  
  else{
    var x = (total_value - (added_value)) / 2.0;
    return x;
  }
  
}

