function gameOfFives(bavarianBeerBears,scandinavianSchöllers){
  var count = 0;
  var count1 = 0;
  
  for (var i = 0; i < bavarianBeerBears.length; i++){
    if (bavarianBeerBears[i] == 5){
      count = count + 1;
    }
  }
  
  for (var i = 0; i < scandinavianSchöllers.length; i++){
    if (scandinavianSchöllers[i] == 5){
      count1 = count1 + 1;
    }
  }
  
  if (count == count1){
    return "Drinks All Round! Free Beers on Bjorg!"
  }
  else{
    return "Uh Oh! Bjorg's a donut! No beer for anyone!"
  }

}

