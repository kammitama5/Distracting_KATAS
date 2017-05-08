function mixFruit (arr) {
    total = 0;
    var a = arr.toLocaleString().toLowerCase().split(',');
    for (var i = 0; i < a.length; i++){
      if (a[i] == 'banana'){
        total = total + 5;
      }
      else if (a[i] == 'orange'){
        total = total + 5;
      }
      else if (a[i] == 'apple'){
        total = total + 5;
      }
      else if (a[i] == 'lemon'){
        total = total + 5;
      }
      else if (a[i] == 'grapes')
      {
        total = total + 5;
      }
      else if (a[i] == 'avocado'){
        total = total + 7;
      }
      else if (a[i] == 'strawberry'){
        total = total + 7;
      }
      else if (a[i] == 'mango'){
        total = total + 7;
      }
      else{
        total = total + 9;
      }
      
    }
    var avg = total / arr.length;
    return(Math.round(avg))
}
