function express(x, device){
    if (device == 'iPhone'){
      return("Damn")
    }
    else if (device == 'Desktop'){
      return("Sent")
    }
    else if ((device == "Laptop") && (x.length !== 22)){
      return("Damn")
    }
    else if ((device == "Laptop") && (x.length === 22)){
      return("Sent")
    }
    else if ((device == "Macbook") && (x.length !== 22)){
      return("Sent")
    } 
    else if ((device == "Laptop") && (x.length === 22)){
      return("Damn")
    }
    else{
      return("Damn")
    }
}

