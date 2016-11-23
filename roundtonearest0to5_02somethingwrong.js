//Given an array of numbers, return
//an array, with each member of input
//array rounded to a nearest number, 
//divisible by 5
//eg roundToFive([34.5, 56.2, 11, 13])
// should return[35, 55, 10, 15]

function roundToFive(numbers){
  numlength = numbers.length;
  
  var myArray = [];
  
  for (i = 0; i < numlength; i++)
  {
    
    // if numbers 1 through 4, return num
    if (numbers[i] ==  1 | numbers[i] == 2
    | numbers[i] == 3 | numbers[i] ==  4  )
       {
         var myInt = 0
         myArray.push(myInt)
       }
    else if (numbers[i] == 5| numbers[i] == 6 | numbers[i] == 7 |  numbers[i] == 8 | numbers[i] ==9 | numbers[i] == 10)
    {
      var myInt = 10
      myArray.push(myInt)
    }
    // if number mod by 10 is less than 5, return rounded number 53 = 55
    else if (((numbers[i]) % 10) < 5){
      var myInt = (numbers[i] - (numbers[i] % 10) );
      myArray.push(myInt)
    }
    // if number mod by 10 more than 5, return rounded number + 5 => 66 = 70
    else if (((numbers[i]) % 10) > 5){
      
      var myInt = ((numbers[i] - (numbers[i] % 10)) + 5)
      myArray.push(myInt)
    }
    //if number mod by 5 == 5, return number => 55 = 55
    else if (((numbers[i]) % 10) == 5){
      var myInt = (numbers[i])
      myArray.push(myInt)
    }
    // nada
    else
    {
      var myInt = ("None")
      myArray.push(myInt)
    }
    // push this to an array
    
  }
  console.log(myArray)
  return myArray
  
  
}
