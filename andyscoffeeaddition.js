function caffeine(coffee, number) {
    var cof = coffee.toLowerCase()
    var shot; 
    if (cof == "espresso"){
      shot = 1 * number
    }
    else if (cof == "double espresso"){
      shot = 2 * number
    }
    else if (cof == "flat white"){
      shot = 2 * number
    }
    else if (cof == "latte"){
      shot = 1 * number
    }
    else if (cof == "mocha"){
      shot = 2 * number
    }
    else if (cof == "decaf"){
      shot = 0 * number
    }
    
    if (shot == 0){
      return("You haven't even had coffee today!");
    }
    else if (shot < 4){
      return("The doctor won't be worried yet!")
    }
    else if (shot == 4){
      return("You can have 2 more shots then no more!")
    }
    else if (shot == 5){
      return( "You can only have an espresso, latte or a decaf now")
    }
    else if (shot >= 6){
      return("Only decaf for you now!")
    }
}
