function arithmetic(a, b, operator){
    if (operator == "add") {
      console.log(a + b)
    }
    if (operator == "subtract"){
      console.log(a - b)
    }
    if (operator == "multiply"){
      console.log( a * b)
    }
    if (operator == "divide"){
      console.log(a / b)
    }
   
  
  
  
}

arithmetic(1, 2, "add") //returns 3
arithmetic(8,2, "subtract") // returns 6 
arithmetic(5, 2, "multiply") // returns 10 
arithmetic(8, 2, "divide") // returns 4  