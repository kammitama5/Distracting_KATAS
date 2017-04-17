public class LearningJava {
  static int NOD(int a, int b) {  
 if (b == 0) { return a; } else { return (NOD(b, a % b)); 
   } 
 }
 }
