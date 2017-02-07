function runningPace(distance, time)
{     
  
      //console.log(distance, time)
      var a = time.split(":")
      //console.log(a)
      mins = parseInt(a[0])
      secs = parseInt(a[1])
      //console.log(mins, secs)
      
      var tottime = (mins * 60) + secs
      
      var speed = tottime / distance
      
      var min1 = parseInt(speed / 60)
      var sec1 = parseInt(speed % 60.0) 
      
      
      if (sec1 == 0){
        return(min1.toString() + ':' + '00')
      }
      else if (sec1 == 1){
        return(min1.toString() + ':' + '01')
      }
      else{
        return((min1.toString() + ':' + sec1.toString()))
      }
      
}
