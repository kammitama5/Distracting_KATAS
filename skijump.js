Jump length = (mountain height * speed * 9) / 10. 
Speed = mountain height * 1.5.

___X_<- you on top of a 5 row mountain!
*****\ 
******\
*******\
********\
*********\.____/

function skiJump(mountain){
    var speed = mountain.length * 1.5
    var jump = ((speed * mountain.length * 9) / 10).toFixed(2)
    
    if (jump < 10){
      return jump + " metres: He's crap!"
    }
    else if ((jump > 10) && (jump < 25))
    {
      return(jump + " metres: He's ok!")
    }
    else if ((jump > 10) && (jump < 50))
    {
      return(jump + " metres: He's flying!")
    }
    else {
      return(jump + " metres: Gold!!")
    }
    return
}
