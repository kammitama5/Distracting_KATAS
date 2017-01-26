
function maxDiff(list) {
      if (list.length == 0){
        return(0)
      }
      else{
        a = (Math.max.apply( Math, list ))
        b = (Math.min.apply( Math, list ))
        return(a - b)
      }
};
