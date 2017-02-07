public class Factorial {

  public int factorial(int n) {
    int fact = 1;
    if (n == 0){
      return 1;
    }
    else if (n < 0){
       throw new IllegalArgumentException();
    }
    else if (n > 12){
        throw new IllegalArgumentException();
    }
    else{
    for (int i = 1; i <= n; i++){
      fact = fact * i;
    }
    return fact;
  }
    
    }
    
}
