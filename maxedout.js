function maxedOut(arr) {
        square = 0 
        var maxint =  9007199254740991
        for (var i = 0; i < arr.length; i++){
          square = square + Math.pow(arr[i], 3)
        }
        if (square <= maxint){
          return(square)
        }
        else{
          return("You've pushed me to the max!")
        }
        
}

