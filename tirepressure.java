public class TirePressure {
  public static String checkPressure (int x) {
    if (x < 220){
      return "Too low";
    }
    else if (x == 220){
      return "Optimal";
    }
    else{
      return "Too high";
    }
  }
}

