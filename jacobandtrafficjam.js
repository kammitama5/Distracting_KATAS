function trafficJam(trafficSpeed, jacobSpeed, dist){
  if (trafficSpeed < jacobSpeed){
    return dist / trafficSpeed;
  }
  else{
    return dist / jacobSpeed;
  }
}
