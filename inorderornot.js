function order(input){
      
      var b = input.split('').sort().join('');
      var reverse1 = input.split("").reverse().join("")
      
      if (new String(input).valueOf() == new String(b).valueOf()){
        return('IN ORDER')
      }
      else if(new String(b).valueOf() == new String(reverse1).valueOf()) {
        return('IN REVERSE ORDER')
      }
      else{
        return('OUT OF ORDER')
      }
}

