function isInertial(array){
  evenarr = []
  oddarr = []
  
  var odd = 0 // find out how many odds
  var even = Math.max.apply(null, array); // get max value
  var greater = 0 
  
  
  for (var i = 0; i < array.length; i++){
    if (array[i] % 2 !== 0){
      odd = odd + 1
    }
    if ((array[i] % 2 === 0) && (array[i] !== even)) {
      evenarr.push(array[i])
    }
    if (array[i] % 2 !== 0 ){
      oddarr.push(array[i])
    }
  }
  
  var minodd = Math.min.apply(null, oddarr)
  
  function  isEvery(i, index, array){
    return i < minodd
  }
  var a = evenarr.every(isEvery)
  
  if ((odd > 0) && (even % 2 === 0) && (a == true)){
    return(true)
  }
  else{
    return(false)
  }
  
  // for every value of odd, make sure larger than even arr 
  // output if true for 
  //1. odd > 0 = true 
  //2. max value is even = true 
  // every value of odd is more than even values in arr 
  
  return 
}
