function isPalindromic(a){
   q = a.toString()
   q1 = q.split("").reverse().join("");
   if (q1 == q){
     return true;
     }
  else{
    return false;
    }
}

