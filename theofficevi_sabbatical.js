function sabb(x, val, happ){
  var x1 = 0;
  for (var i = 0; i < x.length; i++)
  {
    if (x[i] == 's')
    {
      x1 = x1 + 1
    }
    else if (x[i] == 'a'){
      x1 = x1 + 1
    }
    else if (x[i] == 'b'){
      x1 = x1 + 1
    }
    else if (x[i] == 't'){
      x1 = x1 + 1 
    }
    else if (x[i] == 'i'){
      x1 = x1 + 1
    }
    else if (x[i] == 'c'){
      x1 = x1 + 1
    }
    else if (x[i] == 'l'){
      x1 = x1 + 1
    }
  }
  
  var total = x1 + val + happ;
  
  if (total > 22){
    return "Sabbatical! Boom!";
  }
  else{
    return "Back to your desk, boy.";
  }
}

