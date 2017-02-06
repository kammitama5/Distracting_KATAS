function areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) {
      var YL = yourLeft
      var YR = yourRight
      var FL = friendsLeft
      var FR = friendsRight
      
      count = 0 
      count1 = 0 
      
      you = []
      friend = []
      you.push(YL)
      you.push(YR)
      friend.push(FL)
      friend.push(FR)
      
      var a = (Math.max.apply(null,you))
      var b = (Math.max.apply(null,friend))
      
      for (var i = 0; i < you.length; i++){
        count = count + you[i]
      }
      for (var i = 0; i < friend.length; i++){
        count1 = count1 + friend[i]
      }
      
      if ((a == b) && (count == count1)){
        return (true)
      }
      else{
        return (false)
      }
}
