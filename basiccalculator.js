function calculate(num1, operation, num2) {
   if (operation == "+"){
     return num1 + num2

    }
    else if (operation == "-"){
      return num1 - num2
   
    }
    else if ((num2 == 0) && (operation == "*")){
      return 0
    
    }
    else if (operation == "*"){
      return num1 * num2
     
    }
    
    else if (operation == "m"){
      return null
     
    }
    else if ((operation == "/") && (num2 == 0)) {
      return null
       
    }
    else if (operation == "/"){
      return num1 / num2
    
    }
    else{
      return null
    }
    
}

