//Given an array of numbers, return
//an array, with each member of input
//array rounded to a nearest number, 
//divisible by 5
//eg roundToFive([34.5, 56.2, 11, 13])
// should return[35, 55, 10, 15]

function roundToFive(numbers){
  numlength = numbers.length;
  
  for (i = 0; i < numlength; i++)
  {
    // if numbers 1 through 9, return num
    if (numbers[i] ==  1 | numbers[i] == 2
    | numbers[i] == 3 | numbers[i] ==  4 | numbers[i] == 5 |
      numbers[i] == 6 | numbers[i] == 7 |  numbers[i] == 8 | numbers[i] ==9) 
       {
         console.log(numbers[i])
       }
    // if number mod by 10 is less than 5, return rounded number 53 = 55
    else if ((numbers[i]) % 10 < 5){
      console.log(numbers[i] - (numbers[i] % 10) )
    }
    // if number mod by 10 more than 5, return rounded number + 5 => 66 = 70
    else if ((numbers[i]) % 10 > 5){
      
      console.log((numbers[i] - (numbers[i] % 10)) + 5)
    }
    //if number mod by 5 == 5, return number => 55 = 55
    else if (((numbers[i]) % 10) == 5){
      console.log(numbers[i])
    }
    // nada
    else
    {
      console.log("None")
    }
    // push this to an array

  }
  
  
}

roundToFive([34.5, 56.2, 11, 13, 15])
roundToFive([1,5,87,45,8,8])