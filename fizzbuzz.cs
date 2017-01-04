using System;

public static class FizzBuzz{

        public static String CalcFizzBuzz(int n)
        {
            if (n <= 0) {
              return "";
            }
            else if (n % 15 == 0){
              return "Fizz Buzz";
            }
            else if (n % 5 == 0){
              return "Buzz";
            }
            else if (n % 3 == 0){
              return "Fizz";
            }
            else{
              return n.ToString();
            }
        }
}