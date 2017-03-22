var cubeChecker = function(volume, side){
  if ((Math.pow(side, 3)) === volume){
    return true
  }
  else{
    return false
  }
};