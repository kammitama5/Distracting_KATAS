function fourSeasons(d){
//March 20 is 78
//June 20 is 170
//Sept 20 is 262
//Dec 20 is 353
    if (d > 365){
      return("The year flew by!")
    }
    else if (d <= 78){
      return("Winter Season")
    }
    else if ((d <= 170) && (d >= 79)){
      return("Spring Season")
    }
    else if ((d <= 262) && ((d >= 171))){
      return("Summer Season")
    }
    else if ((d <= 353) && (d >= 263)){
      return("Autumn Season")
    }
    else if ((d > 353) && (d <= 365)){
      return("Winter Season")
    }
}
