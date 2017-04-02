function thirstyIn(water, ageOfDwellerArray) {
        var total = 0;
        if (ageOfDwellerArray.length === 0){
          return(-1)
        }
        else{
        for (var i = 0; i < ageOfDwellerArray.length; i++){
          if (ageOfDwellerArray[i] < 18){
            total = total + 1
          }
          else if (ageOfDwellerArray[i] < 50){
            total = total + 2
          }
          else{
            total = total + 1.5
          }
            
        }
        var numdays = water  / total
        return(parseInt(numdays))
        }
}
