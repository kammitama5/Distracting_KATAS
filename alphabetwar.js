function alphabetWar(fight)
{
   var left = 0;
   var right = 0;
   for (var i = 0; i < fight.length; i++){
     if (fight[i] == 'w'){
       left = left + 4;
     }
     else if (fight[i] == 'p')
     {
       left = left + 3;
     }
     else if (fight[i] == 'b')
     {
       left = left + 2;
     }
     else if (fight[i] == 's'){
       left = left + 1;
     }
     else if (fight[i] == 'm'){
       right = right + 4;
     }
     else if (fight[i] == 'q'){
       right = right + 3;
     }
     else if (fight[i] == 'd'){
       right = right + 2;
     }
     else if (fight[i] == 'z'){
       right = right + 1;
     }
     
   }
   if (right == left){
     return("Let's fight again!")
   }
   else if (right > left){
     return("Right side wins!")
   }
   else{
     return("Left side wins!")
   }
}
