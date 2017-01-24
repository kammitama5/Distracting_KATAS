function isSmooth(arr) {
      a = arr.length
      //console.log(a)
      if (a % 2 == 0){
        d = arr[a/2] + arr[((a/2)-1)]
        //console.log(d)
        
        if ((arr[0] == d) && (arr[a - 1] == d)){
          return(true)
        }
        else{
          return(false)
        }
      }
      else{
        c = parseInt(a/2)
        d = arr[c]
        //console.log(d)
        if ((arr[0] == d) && (arr[a - 1] == d)){
          return(true)
        }
        else{
          return(false)
        }
        
      }
      
      
  
  
}
