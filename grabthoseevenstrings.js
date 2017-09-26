function getEvenStrings(str){
      var arr = [];
      for (var i = 0; i < str.length; i++){
        if (i % 2 == 0){
          arr.push(str[i])
        }
      }
   return arr.join('');
}
